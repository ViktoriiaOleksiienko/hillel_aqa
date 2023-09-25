from .base_page import BasePage


class LocalStorage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def save_item(self, key, value):
        self._driver.execute_script(f'localStorage.setItem("{key}", "{value}");')

    def get_item(self, key):
        return self._driver.execute_script(f'return localStorage.getItem("{key}");')