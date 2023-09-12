import time


def test_add_to_basket(product):
    product.add_to_basket()
    time.sleep(5)


def test_read_passage(product):
    product.read_passage()
    time.sleep(5)


def test_see_more_description(product):
    product.see_more_description()
    time.sleep(5)
