from playwright.sync_api import Page

from abilities.control_browser import ControlBrowser
from questions.browser_info_retriever import BrowserInfoRetrieverQuestions


class OpenDuckDuckGo(ControlBrowser, BrowserInfoRetrieverQuestions):
    def __init__(self, page: Page):
        super().__init__(page)

    def perform_opening_duck_duck_go(self, url: str, page_title: str):
        self.navigate_to_url(url)
        self.get_page_title()
        self.is_page_title_correct(page_title)
