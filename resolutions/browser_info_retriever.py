from assertpy import assert_that
from playwright.sync_api import Page

from actions.browser_info_retriever import BrowserInfoRetrieverActions
from utils.logger_formatter import LOGGER


class BrowserInfoRetrieverResolutions:
    def __init__(self, page: Page):
        self._page = page

    def check_page_title(self, title: str):
        page_title = BrowserInfoRetrieverActions(self._page).get_page_title()
        LOGGER.info('', extra={'Page Title': page_title})
        assert_that(title).is_equal_to(page_title)
