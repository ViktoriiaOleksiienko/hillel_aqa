from hw17_page_object_waits.core.base_locators import BaseLocators


class DashboardLocators:
    def __init__(self):
        super().__init__()
        self.banner = ('xpath', '//*[@id="home"]/div/div[2]/div[2]')
        self.promotions = ('xpath', '//*[@id="home"]/div/div[1]/section/div/div[1]/ul/li[1]/a')
        self.readers_choice = ('xpath', '//*[@id="home"]/div/div[2]/div[1]/div[2]/div/ul/li[2]/a')
        self.readers_choice_title = ('xpath', '//*[@id="viewport"]/div[8]/div[1]/div[1]/div[2]/div/h1')
        self.login = ('xpath', '//*[@id="site-header"]/div/div/div[3]/button[2]')
        self.login_modal_window = ('xpath', '//*[@id="viewport"]/div[8]/div[2]/button')
        self.basket = ('xpath', '//*[@id="site-header"]/div/div/div[3]/button[1]')
        self.basket_modal_window = ('xpath', '//*[@id="viewport"]/div[2]/div/div[1]/button')
        self.search = ('xpath', '//*[@id="search"]')
        self.search_button = ('xpath', '//*[@id="site-header"]/div/div/div[2]/div[1]/div/button')