from playwright.sync_api import Page

from utils import LOGGER


class BrowserNavigatorActions:  # pylint: disable=too-few-public-methods
    """
    This class represents actions to navigate a browser page.

    :type: Action
    """

    def __init__(self, page: Page, url: str):
        self._page = page
        self._url = url

    def navigate_to_url(self) -> None:
        """
        Navigate to the given URL.

        :return: None
        """
        LOGGER.info('', extra={'URL': self._url})
        self._page.goto(self._url)
