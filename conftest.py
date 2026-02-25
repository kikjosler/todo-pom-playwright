import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://todomvc.com/examples/react/dist/")
    page.wait_for_load_state("networkidle")
    yield page
    context.close()

@pytest.fixture(scope="function")
def todo_page(page):
    from pages.todo_page import TodoPage
    return TodoPage(page)
