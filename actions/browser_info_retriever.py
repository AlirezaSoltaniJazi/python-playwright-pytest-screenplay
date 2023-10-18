from playwright.sync_api import Page

from utils.logger_formatter import LOGGER


class BrowserInfoRetrieverActions:  # pylint: disable=too-few-public-methods
    """
    This class represents actions to retrieve information from a browser page.

    :type: Action
    """

    def __init__(self, page: Page):
        self._page = page

    def get_page_title(self) -> str:
        """
        Retrieve the title of the current page.


        :return: The title of the current page as a string.
        """
        page_title = self._page.title()
        LOGGER.info('', extra={'Page Title': page_title})
        return page_title
