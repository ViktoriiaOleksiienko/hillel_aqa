import time


def test_go_to_discounts(dashboard):
    dashboard.go_to_discounts()


def test_go_to_login_form(dashboard):
    dashboard.go_to_login_form()


def test_go_to_basket(dashboard):
    dashboard.go_to_basket()


def test_search_book1(dashboard):
    dashboard.search_book1('Розум убивці')
    time.sleep(5)


def test_search_book2(dashboard):
    dashboard.search_book2('Джерело')
    time.sleep(5)
