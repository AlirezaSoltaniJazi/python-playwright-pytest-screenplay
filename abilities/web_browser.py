from playwright.sync_api import Page

from actions import GetPageTitle, OpenURL
from base import BaseAbility
from questions import BrowserInfoRetrieverQuestions


class BrowseTheWeb(BaseAbility):
    def __init__(self, page: Page):
        self._page = page

    def perform_navigate_to_url(self, url: str) -> None:
        OpenURL(self._page, url).perform_as()

    def perform_get_page_title(self) -> str:
        return GetPageTitle(self._page).perform_as()

    def ask_is_page_title_correct(self, page_title: str):
        BrowserInfoRetrieverQuestions(self._page).check_page_title(page_title)
