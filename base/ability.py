from abc import ABC, abstractmethod


class BaseAbility(ABC):  # pylint: disable=too-few-public-methods
    @abstractmethod
    def __init__(self):
        pass
