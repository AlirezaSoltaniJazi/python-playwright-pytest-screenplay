from playwright.sync_api import Page

from base import BaseAction
from utils import LOGGER


class GetPageTitle(BaseAction):  # pylint: disable=too-few-public-methods
    def __init__(self, page: Page):
        self._page = page

    def _get_page_title(self) -> str:
        page_title = self._page.title()
        LOGGER.info('', extra={'Page Title': page_title})
        return page_title

    def perform_as(self) -> str:
        return self._get_page_title()
