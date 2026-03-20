import asyncio
import logging
import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from bot.main import broadcast
from checker.check import Checker

load_dotenv()
logging.basicConfig(level=logging.INFO)

SITES = ["144.31.112.219"]

token = os.getenv("TOKEN")
if token is not None:
    logging.info("Bot starting")
    app = ApplicationBuilder().token(token).build()
    logging.info("Bot created")


async def main():
    await app.initialize()
    await app.start()
    for site in SITES:
        if not Checker(site).is_site_up():
            text = f"ON NO!!! SITE {site} IS DOWN"
            logging.warning(f"Site {site} is not available")
            await broadcast(text, app)
    await app.stop()


if __name__ == "__main__":
    asyncio.run(main())
