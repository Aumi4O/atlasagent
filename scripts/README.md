## `telegram_notify.py`

Sends a Telegram message when the agent needs human help (CAPTCHA, OTP, 2FA, approval).

```bash
python3 scripts/telegram_notify.py --reason captcha --detail "Upwork login"
```

Setup: [docs/TELEGRAM_ASSISTANCE.md](../docs/TELEGRAM_ASSISTANCE.md). Variables: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` in `.env`.

---

Other ideas for later:

- bootstrap logs
- validate yaml
- export application summaries
