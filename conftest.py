import pytest
import os
from playwright.sync_api import sync_playwright
from pages.todo_page import TodoPage

@pytest.fixture(scope="session")
def browser(playwright):
    """РЕЖИМЫ BROWSER"""
    # CI (GitHub) = headless, LOCAL = видимый, DEMO = медленный
    is_ci = os.getenv('CI', 'false').lower() == 'true'
    is_demo = os.getenv('DEMO_MODE', 'false').lower() == 'true'
    
    browser = playwright.chromium.launch(
        headless=is_ci, 
        slow_mo=1500 if is_demo else 500 if not is_ci else 0  # DEMO=медленный
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """НОВАЯ ВКЛАДКА для каждого теста"""
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="function")
def todo_page(page):
    """ГОТОВАЯ TodoMVC страница (POM объект!)"""
    page.goto("https://todomvc.com/examples/react/#/")
    page.wait_for_load_state("networkidle")
    return TodoPage(page)
