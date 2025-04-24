# 🤖 2Captcha Telegram Bot

A simple Telegram bot built with Python that:

- Sends your current [2captcha](https://2captcha.com/) account balance to a Telegram group **every day at specified time**.
- Responds to the `/balance` command to show the current balance on demand.

---

## 📦 Features

- ✅ Scheduled daily balance check (via APScheduler)
- ✅ Responds to `/balance` in a Telegram chat
- ✅ Lightweight and runs in Docker
- ✅ Environment-based configuration

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/2captcha-telegram-bot.git
cd 2captcha-telegram-bot
```

### 2. Create a .env file based on example.env

```bash
API_KEY=your_2captcha_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=-12345678910
```
ℹ️ Note: You can get a bot token by talking to @BotFather in Telegram.

### 3. Start with Docker Compose

```bash
docker compose up --build -d
```

Your bot will now be running and will:
- Post the 2captcha balance every day at 9:00 AM and 6:00 PM (Kyiv time)
- Respond to the /balance command instantly

## 💬 How to Get Your Telegram Group Chat ID
To allow the bot to send messages to your Telegram group:
1. Add your bot to the group and promote it to an admin.
2. Use this bot or the method below to get the group chat_id:
   - Send any message in the group.
   - Open this URL in your browser (replace BOT_TOKEN with your bot token):
   ```http request
    https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
    ```
   - Look for the "chat":{"id":-XXXXXXXXX,...} section.
   - Copy the negative number -XXXXXXXXX as your TELEGRAM_CHAT_ID.

✅ The chat ID for groups is always negative. For example: -1001234567890