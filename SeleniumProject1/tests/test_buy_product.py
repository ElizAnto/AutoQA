import allure

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage

"""Дымовое тестирование покупки товара"""

# @pytest.mark.order(3)
@allure.description("Test buy product 1")
def test_buy_product_1(set_up, driver):
    """sauce-labs-backpack"""
    print("Start test 1")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_products_1()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = ClientInformationPage(driver)
    cip.input_information()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    print("Finish test 1")

@allure.description("Test buy product 2")
def test_buy_product_2(set_up, driver):
    """sauce-labs-bike-light"""
    print("Start test 2")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_products_2()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = ClientInformationPage(driver)
    cip.input_information()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    print("Finish test 2")

@allure.description("Test buy product 3")
def test_buy_product_3(set_up, driver):
    """sauce-labs-bolt-t-shirt"""

    print("Start test 3")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_products_3()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = ClientInformationPage(driver)
    cip.input_information()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    print("Finish test 3")