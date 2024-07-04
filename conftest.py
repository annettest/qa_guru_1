import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def browser_min():
    browser.config.browser_name = 'firefox'
    browser.config.window_height = 800
    browser.config.window_width = 800
    browser.open('https://google.com')
