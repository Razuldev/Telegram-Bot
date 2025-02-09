import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler

import os
from aibot import replyToUser

TOKEN = "add your token here"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

logging.getLogger("httpx").setLevel(logging.WARNING)

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = await replyToUser(user_message)
    await update.message.reply_text(response.content)
    await log_infos(update,response.content)


async def log_infos(update: Update,response : str):
    message = update.message
    user = message.from_user
    chat = message.chat
    logger.info(
        "Yeni mesaj alındı:\n"
        "  User ID: %s\n"
        "  Username: %s\n"
        "  Ad: %s\n"
        "  Soyad: %s\n"
        "  Dil: %s\n"
        "  Chat ID: %s\n"
        "  Mesaj: %s\n"
        "  Cavab: %s",
        user.id,
        user.username or "N/A",
        user.first_name,
        user.last_name or "N/A",
        user.language_code,
        chat.id,
        message.text,
        response
    )


async def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "Salam! 👋 Mən Rəsul haqqında suallarınıza cavab verən asistentəm.\n\n"
        "Nə öyrənmək istəsəniz, çəkinmədən yazın! 😄"
    )
    await update.message.reply_text(welcome_text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
