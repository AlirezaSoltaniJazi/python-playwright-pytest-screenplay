"""
This module contains tasks
"""
from playwright.sync_api import Page
from pytest import mark

from actors.actor import Actor


@mark.search
def test_duck_duck_go_search(page: Page):
    url = 'https://www.duckduckgo.com'
    title = 'DuckDuckGo — Privacy, simplified.'
    the_actor = Actor(page, 'Alireza Soltani Jazi')

    # Given the actor navigates to the DuckDuckGo homepage
    the_actor.navigate_to_url(url)
    # When the actor retrieves the title of the page
    the_actor.get_page_title()
    # Then the actor verifies that the page title is correct
    the_actor.is_page_title_correct(title)
