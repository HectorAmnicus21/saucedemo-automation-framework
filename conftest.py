import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="function")
def page():
    """
    Launches a fresh browser + page for every single test.
    'function' scope = isolation: no test can leak state into another.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True to run silently
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        yield page  # test runs here

        context.close()
        browser.close()