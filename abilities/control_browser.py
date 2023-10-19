"""
This module provides the ControlBrowser class which represents the ability to control a browser.
It includes navigating to a URL and retrieving the page title.
"""
from playwright.sync_api import Page

from actions import BrowserInfoRetrieverActions, BrowserNavigatorActions


class ControlBrowser:
    """
    This class represents the ability to control a browser.
    It includes methods to navigate to a URL and retrieve the page title.

    :type: Ability
    """

    def __init__(self, page: Page):
        self._page = page

    def navigate_to_url(self, url: str) -> None:
        """
        Navigate to a given URL.

        :param url: The URL to navigate to.
        :return: None
        """
        browser_navigation = BrowserNavigatorActions(self._page, url)
        browser_navigation.navigate_to_url()

    def get_page_title(self) -> str:
        """
        Retrieve the title of the current page.

        :return: The title of the current page as a string.
        """
        browser_info = BrowserInfoRetrieverActions(self._page)
        return browser_info.get_page_title()
