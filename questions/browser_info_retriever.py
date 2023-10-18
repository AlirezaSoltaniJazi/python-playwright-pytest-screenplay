from playwright.sync_api import Page

from resolutions.browser_info_retriever import BrowserInfoRetrieverResolutions


class BrowserInfoRetrieverQuestions:
    def __init__(self, page: Page):
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
