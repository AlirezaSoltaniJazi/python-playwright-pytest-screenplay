from playwright.sync_api import Page

from base import BaseAction
from utils import LOGGER


class OpenURL(BaseAction):  # pylint: disable=too-few-public-methods
    def __init__(self, page: Page, url: str):
        self._page = page
        self._url = url

    def _navigate_to_url(self) -> None:
        LOGGER.info('', extra={'URL': self._url})
        self._page.goto(self._url)

    def perform_as(self):
        self._navigate_to_url()
