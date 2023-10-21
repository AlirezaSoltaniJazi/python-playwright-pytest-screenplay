from playwright.sync_api import Page

from actions import OpenURL
from base import BaseTask


class OpenDuckDuckGoPageTask(BaseTask):  # pylint: disable=too-few-public-methods
    def __init__(self, url: str, page: Page):
        self._url = url
        self._page = page

    def _perform_opening_duck_duck_go_page(self):
        OpenURL(self._page, self._url).perform_as()

    def perform_as(self):
        self._perform_opening_duck_duck_go_page()
