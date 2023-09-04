from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


def test_1():
    driver = Chrome()
    driver.get('https://www.yakaboo.ua/')
    search_field_locator = '//*[@id="search"]'
    first_element = driver.find_element(by='xpath', value=search_field_locator)
    first_element.send_keys('Хірург')
    first_element.send_keys(Keys.ENTER)
    time.sleep(5)


def test_2():
    driver = Chrome()
    driver.get('https://www.yakaboo.ua/')
    search_field_locator = '//*[@id="search"]'
    first_element = driver.find_element(by='xpath', value=search_field_locator)
    first_element.send_keys('Хірург')
    first_element.send_keys(Keys.ENTER)
    time.sleep(2)
    first_book_locator = '//*[@id="viewport"]/div[8]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/a'
    first_book = driver.find_element(by='xpath', value=first_book_locator)
    assert first_book.text == 'Хірург. Книга 1'
    first_book.click()
    time.sleep(5)


def test_3():
    driver = Chrome()
    driver.get('https://www.yakaboo.ua/')
    search_field_locator = '//*[@id="search"]'
    first_element = driver.find_element(by='xpath', value=search_field_locator)
    first_element.send_keys('Хірург')
    first_element.send_keys(Keys.ENTER)
    time.sleep(2)
    first_book_locator = '//*[@id="viewport"]/div[8]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/a'
    first_book = driver.find_element(by='xpath', value=first_book_locator)
    assert first_book.text == 'Хірург. Книга 1'
    first_book.click()
    time.sleep(2)
    second_page_locator = '//*[@id="product"]/div[1]/div/div/div/section/div[9]/section/div/div[3]/div[2]/div/button[2]/a'
    second_page = driver.find_element(by='xpath', value=second_page_locator)
    second_page.click()
    time.sleep(5)


def test_4():
    driver = Chrome()
    driver.get('https://www.yakaboo.ua/')
    search_field_locator = '//*[@id="search"]'
    first_element = driver.find_element(by='xpath', value=search_field_locator)
    first_element.send_keys('Хірург')
    first_element.send_keys(Keys.ENTER)
    time.sleep(3)
    price_filter_locator = '//*[@id="viewport"]/div[8]/div[1]/div[2]/div[2]/div[1]/div[2]/div/button[8]'
    price_filter = driver.find_element(by='xpath', value=price_filter_locator)
    price_filter.click()
    time.sleep(2)
    max_price_locator = '/html/body/div[1]/div/div[2]/div[7]/div/div[2]/div/div/aside/div/div/div/div/div[2]/div/div[2]/div/div/input'
    max_price = driver.find_element(by='xpath', value=max_price_locator)
    time.sleep(2)
    max_price.clear()
    time.sleep(2)
    max_price.send_keys('200')
    time.sleep(2)
    apply_button_locator = '//*[@id="viewport"]/div[7]/div/div[2]/div/div/aside/div/div/div/div/div[2]/div/button'
    apply_button = driver.find_element(by='xpath', value=apply_button_locator)
    apply_button.click()
    time.sleep(5)


def test_5():
    driver = Chrome()
    driver.get('https://www.yakaboo.ua/')
    search_field_locator = '//*[@id="search"]'
    first_element = driver.find_element(by='xpath', value=search_field_locator)
    first_element.send_keys('Хірург')
    first_element.send_keys(Keys.ENTER)
    time.sleep(2)
    first_book_locator = '//*[@id="viewport"]/div[8]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[2]/a'
    first_book = driver.find_element(by='xpath', value=first_book_locator)
    assert first_book.text == 'Хірург. Книга 1'
    first_book.click()
    time.sleep(2)
    passage_locator = '//*[@id="product"]/div[1]/div/div/section[1]/div[3]/div[1]/button'
    passage = driver.find_element(by='xpath', value=passage_locator)
    passage.click()
    time.sleep(5)
