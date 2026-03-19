from telegram import Update
from telegram.ext import Application, ContextTypes

subscribed_users = set()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update is not None and update.effective_chat is not None:
        subscribed_users.add(update.effective_chat.id)
        if update.message is not None:
            await update.message.reply_text("Subscribed to updates!")


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update is not None and update.effective_chat is not None:
        if update.effective_chat.id in subscribed_users:
            subscribed_users.remove(update.effective_chat.id)
        if update.message is not None:
            await update.message.reply_text("Unsubscribed")


async def broadcast(text: str, app: Application):
    for chat_id in subscribed_users:
        await app.bot.send_message(chat_id=chat_id, text=text)
