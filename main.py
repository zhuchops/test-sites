import asyncio
import logging
import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from bot.main import start, stop
from checker.check import Checker

load_dotenv()
logging.basicConfig(level=logging.INFO)

SITES = ["https://google.com", "https://httpstat.us/500"]

token = os.getenv("TOKEN")
if token is not None:
    logging.info("Bot starting")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    logging.info("Bot created")


async def main():
    async with app:
        await app.start()
        if app.updater is not None:
            await app.updater.start_polling()

        await asyncio.gather(*map(lambda x: Checker(x, app).run(), SITES))


if __name__ == "__main__":
    asyncio.run(main())
