"""
The module represents the control browser ability.
"""
from playwright.sync_api import Page

from actions.browser_navigator import BrowserNavigatorActions
from actions.browser_info_retriever import BrowserInfoRetrieverActions


class ControlBrowser:
    def __init__(self, page: Page):
        self._page = page

    def navigate_to_url(self, url: str) -> None:
        """
        Represent the ability for navigating to a URL
        :return: None
        """
        browser_navigation = BrowserNavigatorActions(self._page, url)
        browser_navigation.navigate_to_url()

    def get_page_title(self) -> str:
        """
        Represent the ability for getting the page title
        :return: The page title
        """
        browser_info = BrowserInfoRetrieverActions(self._page)
        return browser_info.get_page_title()
