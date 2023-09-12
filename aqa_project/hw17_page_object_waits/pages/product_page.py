from hw17_page_object_waits.pages.base_page import BasePage
from hw17_page_object_waits.core.product_locators import ProductsLocator


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductsLocator()

    def add_to_basket(self):
        self.click_to_element(self.locators.add_to_basket)

    def read_passage(self):
        self.click_to_element(self.locators.read_passage_button)

    def see_more_description(self):
        self.click_to_element(self.locators.see_more)
