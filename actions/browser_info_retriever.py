from playwright.sync_api import Page

from utils.logger_formatter import LOGGER


class BrowserInfoRetrieverActions:
    def __init__(self, page: Page):
        self._page = page

    def get_page_title(self) -> str:
        page_title = self._page.title()
        LOGGER.info('', extra={'Page Title': page_title})
        return page_title
