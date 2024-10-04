API="7795328391:AAFXLIlN66jnoRKtQOKKKOcAQlZ3EmBgqoo"

import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters, ContextTypes, Application
# from app import linkedIn


async def start(update: Update, context: CallbackContext):
    print("start")
    await update.message.reply_text('Hello! I am your bot.')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Here are the available commands...')


async def handle_message(update: Update, context: CallbackContext):
    text= update.message.text
    
    await update.message.reply_text("Searching jobs")
    # linkedIn()
    await update.message.reply_text("Applied jobs")
    



def main():
    application = ApplicationBuilder().token(API).build()

    # Command Handler
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Message Handler
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
