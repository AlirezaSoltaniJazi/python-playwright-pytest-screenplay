"""
This module contains tasks
"""
from playwright.sync_api import Page
from pytest import mark

from actors import NormalUserActor


@mark.search
def test_duck_duck_go_search(page: Page):
    # Given the actor navigates to the DuckDuckGo homepage
    # When the actor retrieves the title of the page
    # Then the actor verifies that the page title is correct

    url = 'https://www.duckduckgo.com'
    title = 'DuckDuckGo — Privacy, simplified.'

    the_actor = NormalUserActor('Alireza Soltani Jazi', page)
    the_actor.perform_navigate_to_url(url)
    the_actor.ask_is_page_title_correct(title)
