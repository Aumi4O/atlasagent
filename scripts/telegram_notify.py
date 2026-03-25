#!/usr/bin/env python3
"""
Send a Telegram message when Atlas Agent hits CAPTCHA, OTP, 2FA, or other blockers.

Requires in .env (or environment):
  TELEGRAM_BOT_TOKEN  — from @BotFather
  TELEGRAM_CHAT_ID    — numeric id of you or a group (see docs/TELEGRAM_ASSISTANCE.md)

Usage:
  python scripts/telegram_notify.py --reason captcha
  python scripts/telegram_notify.py --reason otp --detail "LinkedIn sign-in"
  python scripts/telegram_notify.py "Custom one-line message"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

TELEGRAM_SEND = "https://api.telegram.org/bot{token}/sendMessage"

PRESETS: dict[str, str] = {
    "captcha": "Atlas Agent: CAPTCHA / bot check — please complete in the browser, then tell me to continue.",
    "otp": "Atlas Agent: OTP / SMS / email verification code needed.",
    "2fa": "Atlas Agent: 2FA step — please complete verification.",
    "approval": "Atlas Agent: waiting for your approval before final submit.",
    "blocked": "Atlas Agent: flow blocked — need your decision or manual step.",
    "generic": "Atlas Agent: human assistance needed.",
}


def load_dotenv() -> None:
    """Load .env from repo root if present (no external dependency)."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, ".env")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val


def send_message(token: str, chat_id: str, text: str) -> dict:
    url = TELEGRAM_SEND.format(token=token)
    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": True,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Notify via Telegram for Atlas Agent assistance.")
    parser.add_argument(
        "message",
        nargs="*",
        help="Free-form message (if empty, use --reason)",
    )
    parser.add_argument(
        "--reason",
        choices=sorted(PRESETS.keys()),
        help="Preset message for common blockers",
    )
    parser.add_argument(
        "--detail",
        default="",
        help="Extra line appended after preset or custom message",
    )
    args = parser.parse_args()

    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        print("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID (.env or environment).", file=sys.stderr)
        print("See docs/TELEGRAM_ASSISTANCE.md", file=sys.stderr)
        return 2

    if args.message:
        text = " ".join(args.message).strip()
    elif args.reason:
        text = PRESETS[args.reason]
    else:
        text = os.environ.get("TELEGRAM_MESSAGE", PRESETS["generic"])

    if args.detail:
        text = f"{text}\n\n{args.detail.strip()}"

    if len(text) > 4096:
        text = text[:4093] + "..."

    try:
        result = send_message(token, chat_id, text)
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        print(f"Telegram HTTP {e.code}: {err}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"Telegram network error: {e}", file=sys.stderr)
        return 1

    if not result.get("ok"):
        print(result, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
