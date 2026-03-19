import os

from telegram.ext import Application

subscribed_users = set()


async def broadcast(text: str, app: Application):
    await app.bot.send_message(chat_id=os.getenv("CHAT_ID"), text=text)
