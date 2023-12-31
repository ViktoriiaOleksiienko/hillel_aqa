import time


def test_category_page_functionality(categories):
    cookies_manager = categories.cookies
    local_storage_manager = categories.local_storage
    category_page = categories
    print("Saving cookies...")
    cookies_manager.save_cookie("user_id", "007")
    user_id_cookie = cookies_manager.get_cookie("user_id")
    print("Saving local storage...")
    local_storage_manager.save_item("token", "4е35ре84ре")
    token_local_storage = local_storage_manager.get_item("token")
    time.sleep(40)


def test_go_to_first_card(dashboard):
    category_page = dashboard.go_to_readers_choice()
    product_page = category_page.go_to_first_card()
    time.sleep(5)


def test_filtered_sale(dashboard):
    category_page = dashboard.go_to_readers_choice()
    category_page.filter_sale()
    product_page = category_page.go_to_first_card()
    time.sleep(5)


def test_filtered_sale_start_from_categories(categories):
    categories.filter_sale()
    product_page = categories.go_to_first_card()
    time.sleep(5)


def test_go_to_second_card(categories):
    categories.go_to_second_card()
    product_page = categories.go_to_second_card()
    time.sleep(5)


def test_go_to_second_page(categories):
    categories.go_to_second_page()
    product_page = categories.go_to_second_page()
    time.sleep(5)