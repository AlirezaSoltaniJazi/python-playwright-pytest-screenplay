from abc import ABC, abstractmethod

from playwright.sync_api import Page


class BaseActor(ABC):  # pylint: disable=too-few-public-methods
    @abstractmethod
    def __init__(self, name: str, page: Page):
        pass
