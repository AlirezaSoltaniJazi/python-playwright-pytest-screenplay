from abc import ABC, abstractmethod


class BaseAction(ABC):  # pylint: disable=too-few-public-methods
    @abstractmethod
    def perform_as(self):
        pass
