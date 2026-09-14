from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я твій Telegram-бот 🤖")

async def echo(update: Update, context):
    await update.message.reply_text(f"Ти написав: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()
