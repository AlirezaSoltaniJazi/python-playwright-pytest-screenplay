from playwright.sync_api import Page

from utils.logger_formatter import LOGGER


class BrowserNavigatorActions:
    def __init__(self, page: Page, url: str):
        self._page = page
        self._url = url

    def navigate_to_url(self) -> None:
        LOGGER.info('', extra={'URL': self._url})
        self._page.goto(self._url)
