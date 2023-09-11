import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_discounts(dashboard):
    dashboard.go_to_discounts()
    WebDriverWait(dashboard._driver, 10).until(EC.url_contains('https://www.yakaboo.ua/ua/promotions'))


def test_go_to_login_form(dashboard):
    dashboard.go_to_login_form()
    WebDriverWait(dashboard._driver, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="viewport"]/div[8]/div[2]/div')))


def test_go_to_basket(dashboard):
    dashboard.go_to_basket()
    WebDriverWait(dashboard._driver, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="viewport"]/div[2]/div/div[1]/button')))


def test_search_book1(dashboard):
    dashboard.search_book1('Розум убивці')
    time.sleep(5)


def test_search_book2(dashboard):
    dashboard.search_book2('Джерело')
    time.sleep(5)
