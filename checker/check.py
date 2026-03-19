import logging

import requests
from telegram.ext import Application

from bot.main import broadcast


class Checker:
    url: str

    def __init__(self, url: str) -> None:
        self.url = url

    def is_site_up(self) -> bool:
        try:
            r = requests.get(self.url, timeout=5)
            logging.info(f"Site {self.url} is available")
            return r.status_code < 500
        except requests.RequestException:
            return False
