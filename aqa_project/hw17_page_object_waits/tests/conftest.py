from selenium.webdriver import Chrome
from hw17_page_object_waits.pages.dashboard_page import Dashboard
from hw17_page_object_waits.pages.category_page import CategoryPage
from hw17_page_object_waits.pages.product_page import ProductPage
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def dashboard(driver):
    driver.get('https://www.yakaboo.ua/')
    yield Dashboard(driver)


@pytest.fixture
def categories(driver):
    driver.get('https://www.yakaboo.ua/ua/knigi/vibir-chitachiv.html')
    yield CategoryPage(driver)


@pytest.fixture()
def product(driver):
    driver.get('https://www.yakaboo.ua/ua/ja-bachu-vas-cikavit-pit-ma.html')
    yield ProductPage(driver)
