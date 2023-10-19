from playwright.sync_api import Page

from tasks.duck_duck_go import DuckDuckGoTasks


class NormalUserActor(DuckDuckGoTasks):
    """
    This class represents an Actor who can control a browser and retrieve information from it.

    :type: Actor
    """

    def __init__(self, page: Page, name: str):
        """
        Initialize the Actor with a page and a name.

        :param page: The Page object from playwright.
        :param name: The name of the Actor.
        """
        super().__init__(page)
        self._the_actor = name

    def __str__(self):
        """
        Return a string representation of the Actor.

        :return: A string that represents the Actor.
        """
        return f'The actor name is: {self._the_actor}'
