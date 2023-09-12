from hw17_page_object_waits.core.base_locators import BaseLocators


class CategoriesLocator(BaseLocators):
    def __init__(self):
        super().__init__()
        self.checkbox_sale = ('xpath', '//*[@id="viewport"]/div[8]/div[1]/div[3]/div[1]/aside/div/div[1]/div/div/div[2]/a[1]')
        self.first_card = ('xpath', '//*[@id="viewport"]/div[8]/div[1]/div[3]/div[2]/div[2]/div/div[1]/div')
        self.second_card = ('xpath', '//*[@id="viewport"]/div[8]/div[1]/div[3]/div[2]/div[2]/div/div[2]/div')
        self.second_page = ('xpath', '//*[@id="viewport"]/div[8]/div[1]/div[3]/div[2]/div[3]/div/div/div/div[2]')
