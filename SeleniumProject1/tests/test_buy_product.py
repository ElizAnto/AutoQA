from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_buy_product():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(),
                              service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))

    print("Start test")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_product()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = ClientInformationPage(driver)
    cip.input_information()

    p = PaymentPage(driver)
    p.payment()

    f = FinishPage(driver)
    f.finish()

    print("Finish test")