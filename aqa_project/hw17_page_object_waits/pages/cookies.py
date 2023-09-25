from .base_page import BasePage


class Cookies(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def save_cookie(self, name, value):
        self._driver.add_cookie({"name": name, "value": value})

    def get_cookie(self, name):
        return self._driver.get_cookie(name)