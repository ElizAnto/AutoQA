from pages.cart_page import CartPage
from pages.clear_cart_page import ClearCartPage
from pages.client_information_page import ClientInformationPage
from pages.filters_page import SmartFiltersPage
from pages.login_page import LoginPage
from pages.main_page import SmartPage
from pages.product_page import ProductPage
import allure

"""Дымовое тестирование покупки товара 'Смартфон Xiaomi Redmi Note 14 8/128GB Черный'"""
@allure.description("Test buy phone")
def test_buy_phone(set_up, driver):

    login = LoginPage(driver)
    login.authorisation()

    smart = SmartPage(driver)
    smart.search_smart()

    filters = SmartFiltersPage(driver)
    filters.choose_filters()

    product = ProductPage(driver)
    product.select_product()

    cart = CartPage(driver)
    cart.product_confirmation()

    client_information = ClientInformationPage(driver)
    client_information.input_information()

    clear_cart = ClearCartPage(driver)
    clear_cart.clear_cart()