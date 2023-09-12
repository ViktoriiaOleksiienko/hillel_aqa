
class BaseLocators:
    def __init__(self):
        self.category = ('xpath', '//*[@id="site-header"]/div/div/div[2]/button')
        self.basket = ('xpath', '//*[@id="site-header"]/div/div/div[3]/button[1]')
        self.search = ('xpath', '//*[@id="search"]')
