# Telegram alerts for human assistance

When Atlas Agent hits **CAPTCHA**, **OTP**, **2FA**, **email verification**, or needs **approval**, run the notifier so you get a push on your phone.

## 1. Create a bot

1. Open Telegram, chat with [@BotFather](https://t.me/BotFather).
2. Send `/newbot`, follow prompts, copy the **HTTP API token**.

## 2. Get your chat id

**Private chat (messages to you):**

1. Start a chat with your new bot (tap **Start**).
2. Send any message to the bot.
3. Open in a browser (replace `TOKEN`):

   `https://api.telegram.org/botTOKEN/getUpdates`

4. Find `"chat":{"id":123456789` — that number is `TELEGRAM_CHAT_ID`.

**If another bot already showed your ID:** some bots print “Your Telegram ID: `…`”. That number is usually your **user id** — you can paste it into `TELEGRAM_CHAT_ID` for Atlas alerts (same as step 4).

**Group (optional):** add the bot to the group, send a message mentioning the bot or any message, then call `getUpdates` again and use the group’s negative `chat.id`.

## 3. Configure locally

In `.env` (never commit):

```bash
TELEGRAM_BOT_TOKEN=123456:ABC-DEF...
TELEGRAM_CHAT_ID=123456789
```

## 4. Send a test

From the repository root:

```bash
python3 scripts/telegram_notify.py --reason generic
python3 scripts/telegram_notify.py --reason captcha --detail "Platform: Upwork"
```

Or a custom line:

```bash
python3 scripts/telegram_notify.py "Atlas paused: complete login in browser"
```

## 5. Wire into workflows

- **Cursor / scripts:** call `telegram_notify.py` right after writing a checkpoint when a blocker is detected.
- **ChatGPT / manual:** paste the same command into a terminal on the machine where `.env` lives, or ask the coding agent to run it when you confirm a blocker.

## Security

- The bot token is a **secret** — same rules as passwords: `.env` only, not git, not screenshots in chats.
- This sends **outbound notifications only**. It does not read your Telegram replies to resume automation (that would need a separate long-running bot process).

## Troubleshooting

| Issue | What to check |
|--------|----------------|
| `403 Forbidden` / bot can’t initiate | You must **Start** the bot in Telegram first. |
| Wrong chat | Use `getUpdates` after you message the bot from the intended account or group. |
| Empty `getUpdates` | Send a new message to the bot, refresh the URL. |
