from assertpy import assert_that
from playwright.sync_api import Page

from actions import GetPageTitle
from base import BaseResolution
from utils import LOGGER


class BrowserInfoRetrieverResolutions(
    BaseResolution
):  # pylint: disable=too-few-public-methods
    def __init__(self, page: Page):
        self._page = page

    def assert_page_title(self, title: str):
        page_title = GetPageTitle(self._page).perform_as()
        LOGGER.info('', extra={'Page Title': page_title})
        assert_that(title).is_equal_to(page_title)
