from hw17_page_object_waits.core.base_locators import BaseLocators


class ProductsLocator(BaseLocators):
    def __init__(self):
        super().__init__()
        self.add_to_basket = ('xpath', '//*[@id="product"]/div[1]/div/div/section[2]/div/div/div[4]/button[2]')
        self.read_passage_button = ('xpath', '//*[@id="product"]/div[1]/div/div/section[1]/div[3]/div[1]/button')
        self.see_more = ('xpath', '//*[@id="product"]/div[1]/div/div/div/section/div[3]/div/button')
