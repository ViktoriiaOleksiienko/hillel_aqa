import time
from hw17_page_object_waits.pages.base_page import BasePage


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_discounts(self):
        discounts_button_locator = ('xpath', '//*[@id="home"]/div/div[2]/div[1]/div[2]/div/ul/li[1]/a')
        discounts_page_locator = ('xpath', '//*[@id="viewport"]/div[8]')
        self.wait_until_element_appears(discounts_page_locator)
        self.click_to_element(discounts_button_locator)

    def go_to_login_form(self):
        login_button_locator = ('xpath', '//*[@id="site-header"]/div/div/div[3]/button[2]')
        modal_button_locator = ('xpath', '//*[@id="viewport"]/div[8]/div[2]/button')
        self.click_to_element(login_button_locator)
        self.wait_until_element_clicked(modal_button_locator)
        self.click_to_element(modal_button_locator)

    def go_to_basket(self):
        basket_button_locator = ('xpath', '//*[@id="site-header"]/div/div/div[3]/button[1]')
        modal_button_locator = ('xpath', '//*[@id="viewport"]/div[2]/div/div[1]/button')
        self.click_to_element(basket_button_locator)
        self.wait_until_element_clicked(modal_button_locator)
        self.click_to_element(modal_button_locator)

    def search_book1(self, message):
        field_locator = ('xpath', '//*[@id="search"]')
        search_locator = ('xpath', '//*[@id="site-header"]/div/div/div[2]/div[1]/div/button')
        self.send_keys_to_element(field_locator, message)
        self.click_to_element(search_locator)

    def search_book2(self, message):
        locator = ('xpath', '//*[@id="search"]')
        self.send_keys_to_element(locator, message)
        self.press_enter(locator)
