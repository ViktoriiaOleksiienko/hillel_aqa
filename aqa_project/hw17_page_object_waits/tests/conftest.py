from selenium.webdriver import Chrome
from hw17_page_object_waits.pages.dashboard_page import Dashboard
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://www.yakaboo.ua/')
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)