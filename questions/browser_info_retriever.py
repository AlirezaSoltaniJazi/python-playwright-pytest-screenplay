from playwright.sync_api import Page

from base import BaseQuestion
from resolutions import BrowserInfoRetrieverResolutions


class BrowserInfoRetrieverQuestions(
    BaseQuestion
):  # pylint: disable=too-few-public-methods
    def __init__(self, page: Page):
        self._page = page

    def check_page_title(self, title: str):
        BrowserInfoRetrieverResolutions(self._page).assert_page_title(title)
