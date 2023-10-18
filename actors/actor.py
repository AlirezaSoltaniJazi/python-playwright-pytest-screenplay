from playwright.sync_api import Page

from abilities.control_browser import ControlBrowser
from questions.browser_info_retriever import BrowserInfoRetrieverQuestions


class Actor(ControlBrowser, BrowserInfoRetrieverQuestions):
    def __init__(self, page: Page, name: str):
        super().__init__(page)
        self._the_actor = name

    def __str__(self):
        return f'The actor name is: {self._the_actor}'
