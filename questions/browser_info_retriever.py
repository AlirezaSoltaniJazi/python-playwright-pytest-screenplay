from playwright.sync_api import Page

from resolutions import BrowserInfoRetrieverResolutions


class BrowserInfoRetrieverQuestions:  # pylint: disable=too-few-public-methods
    """
    This class represents questions that validate information retrieved from a browser page.

    :type: Question
    """

    def __init__(self, page: Page):
        """
        Initialize the BrowserInfoRetrieverQuestions with a page.

        :param page: The Page object from playwright.
        """
        self._page = page

    def is_page_title_correct(self, title: str):
        """
        This function represents a question that validates the page title. It uses
        the BrowserInfoRetrieverResolutions to check if the actual title of the page
        matches the expected title.

        :param title: The expected title of the web page.
        :return: None
        """
        BrowserInfoRetrieverResolutions(self._page).check_page_title(title)
