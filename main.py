from telegram import Update
from telegram.ext import (
Application,
CallbackContext,
CommandHandler,
MessageHandler,
filters
)

application = Application.builder().token("5975542604:AAHO23bjFrptYmy3PvoY9b13voBmuamaeEI").build()
print("Successfully connected to Telegram API")
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am a bot that is going to mimic you :)")


async def mimic(update: Update, context: CallbackContext):
    incoming_text = update.message.text
    await update.message.reply_text(incoming_text)


application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters=filters.TEXT, callback=mimic))

application.run_polling()