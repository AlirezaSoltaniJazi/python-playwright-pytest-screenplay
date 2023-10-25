from playwright.sync_api import Page

from abilities import BrowseTheWeb
from base import BaseActor


class NormalUserActor(BaseActor, BrowseTheWeb):
    def __init__(self, name: str, page: Page):
        super().__init__(name, page)
        self._name = name
        self._page = page
