import time
from hw17_page_object_waits.pages.base_page import BasePage
from hw17_page_object_waits.pages.category_page import CategoryPage
from hw17_page_object_waits.core.dashboard_locators import DashboardLocators


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()

    def go_to_readers_choice(self):
        self.click_to_element(self.locators.readers_choice)
        self.wait_until_element_appears(self.locators.readers_choice_title)
        return CategoryPage(self._driver)

    def go_to_login_form(self):
        self.click_to_element(self.locators.login)
        self.wait_until_element_clicked(self.locators.login_modal_window)
        self.click_to_element(self.locators.login_modal_window)

    def go_to_basket(self):
        self.click_to_element(self.locators.basket)
        self.wait_until_element_clicked(self.locators.basket_modal_window)
        self.click_to_element(self.locators.basket_modal_window)

    def search_book1(self, message):
        self.send_keys_to_element(self.locators.search, message)
        self.click_to_element(self.locators.search_button)

    def search_book2(self, message):
        self.send_keys_to_element(self.locators.search, message)
        self.press_enter(self.locators.search)
