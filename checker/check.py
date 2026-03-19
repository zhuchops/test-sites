import asyncio
import logging
from dataclasses import dataclass

import requests
from telegram.ext import Application

from bot.main import broadcast


class Checker:
    url: str
    bot: Application

    def __init__(self, url: str, app: Application) -> None:
        self.url = url
        self.app = app

    async def run(self):
        while True:
            await self._is_site_up()
            await asyncio.sleep(10)

    async def _is_site_up(self) -> bool:
        try:
            r = requests.get(self.url, timeout=5)
            logging.info(f"Site {self.url} is available")
            return r.status_code < 500
        except requests.RequestException:
            text = f"ON NO!!! SITE {self.url} IS DOWN"
            logging.warning(f"Site {self.url} is not available")
            await broadcast(text, self.app)
            return False
