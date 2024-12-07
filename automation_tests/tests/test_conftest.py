
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="automation_tests")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="automation_tests")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
