import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! Saya bot bantuan grant. Sila tanya soalan berkaitan grant, dan saya akan cuba bantu berdasarkan dokumen yang disediakan."
    )

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(
        f"Terima kasih. Nanti saya akan jawab soalan ini berdasarkan PDF grant:\n\n'{user_text}'"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
