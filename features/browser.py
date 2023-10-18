from playwright.sync_api import sync_playwright, BrowserContext, Browser
from pytest import fixture


@fixture(scope='session')
def browser(config):
    browser_config = config['browser']
    headed_mode_config = config['active_headed_mode']
    playwright = sync_playwright().start()
    browser_args = {"headless": False} if headed_mode_config else {}
    browsers = {
        "chrome": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }
    browser_instance = browsers.get(browser_config, browsers['chrome']).launch(
        **browser_args
    )
    yield browser_instance
    browser_instance.close()


@fixture
def context(browser: Browser):
    context_instance = browser.new_context()
    return context_instance


@fixture
def page(context: BrowserContext):
    page_instance = context.new_page()
    yield page_instance
    page_instance.close()
