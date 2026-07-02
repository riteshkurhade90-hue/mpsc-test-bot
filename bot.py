
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BOT_TOKEN
from database import init_db, add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(user.id, user.full_name)

    await update.message.reply_text(
        f"👋 Welcome {user.first_name}!\n\n"
        "📚 MPSC Test Series\n\n"
        "लवकरच Test सुरू होईल."
    )


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
