from abilities.control_browser import ControlBrowser
from questions.browser_info_retriever import BrowserInfoRetrieverQuestions


class DuckDuckGoTasks(ControlBrowser, BrowserInfoRetrieverQuestions):
    def perform_opening_duck_duck_go(self, url: str, page_title: str):
        self.navigate_to_url(url)
        self.is_page_title_correct(page_title)
