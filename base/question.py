from abc import ABC, abstractmethod

from playwright.sync_api import Page


class BaseQuestion(ABC):  # pylint: disable=too-few-public-methods
    @abstractmethod
    def __init__(self, page: Page):
        pass
