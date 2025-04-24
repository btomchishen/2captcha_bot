import os
import logging
import requests
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))

API_URL = "https://api.2captcha.com/"
GET_BALANCE_METHOD = "getBalance"

# Bot init
bot = Bot(token=BOT_TOKEN)


def get_balance_text():
    try:
        response = requests.post(
            API_URL + GET_BALANCE_METHOD,
            json={"clientKey": API_KEY},
            headers={"Content-Type": "application/json"}
        )
        data = response.json()
        if data.get("errorId") == 0:
            return f"💰 Balance 2captcha: {data['balance']:.2f} USD"
        return f"❌ Error 2captcha: {data}"
    except Exception as e:
        return f"🚨 Internal error: {e}"


# For /balance
def balance_command(update: Update, context: CallbackContext):
    balance_text = get_balance_text()
    context.bot.send_message(chat_id=update.effective_chat.id, text=balance_text)


def send_balance():
    text = get_balance_text()
    bot.send_message(chat_id=CHAT_ID, text=text)


def main():
    logging.basicConfig(level=logging.INFO)
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("balance", balance_command))

    scheduler = BackgroundScheduler(timezone=timezone("Europe/Kyiv"))
    scheduler.add_job(send_balance, "cron", hour=9, minute=0)
    scheduler.add_job(send_balance, "cron", hour=18, minute=0)
    scheduler.start()

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
