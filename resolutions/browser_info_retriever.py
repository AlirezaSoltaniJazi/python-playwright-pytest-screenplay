from assertpy import assert_that
from playwright.sync_api import Page

from actions.browser_info_retriever import BrowserInfoRetrieverActions
from utils.logger_formatter import LOGGER


class BrowserInfoRetrieverResolutions:  # pylint: disable=too-few-public-methods
    """
    This class represents resolutions that validate information retrieved from a browser page.

    :type: Resolution
    """

    def __init__(self, page: Page):
        """
        Initialize the BrowserInfoRetrieverResolutions with a page.

        :param page: The Page object from playwright.
        """
        self._page = page

    def check_page_title(self, title: str):
        """
        Check if the actual title of the page matches the expected title.

        :param title: The expected title of the web page.
        :return: None
        """
        page_title = BrowserInfoRetrieverActions(self._page).get_page_title()
        LOGGER.info('', extra={'Page Title': page_title})
        assert_that(title).is_equal_to(page_title)
