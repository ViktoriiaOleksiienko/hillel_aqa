from hw17_page_object_waits.pages.base_page import BasePage
from hw17_page_object_waits.pages.product_page import ProductPage
from hw17_page_object_waits.core.categories_locators import CategoriesLocator


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoriesLocator()

    def go_to_first_card(self):
        self.click_to_element(self.locators.first_card)
        return ProductPage(self._driver)

    def filter_sale(self):
        self.click_to_element(self.locators.checkbox_sale)

    def go_to_second_card(self):
        self.click_to_element(self.locators.second_card)

    def go_to_second_page(self):
        self.click_to_element(self.locators.second_page)
