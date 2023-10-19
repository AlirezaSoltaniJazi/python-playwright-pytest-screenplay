from abilities import ControlBrowser
from questions import BrowserInfoRetrieverQuestions


class DuckDuckGoTasks(ControlBrowser, BrowserInfoRetrieverQuestions):
    def perform_opening_duck_duck_go(self, url: str, page_title: str):
        self.navigate_to_url(url)
        self.is_page_title_correct(page_title)
