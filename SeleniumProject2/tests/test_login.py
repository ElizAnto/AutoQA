from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from pages.cart_page import CartPage
from pages.clear_cart_page import ClearCartPage
from pages.client_information_page import ClientInformationPage
from pages.filters_page import SmartFiltersPage
from pages.login_page import LoginPage
from pages.main_page import SmartPage
from pages.product_page import ProductPage

def test_login():
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'  # Позволяет начинать работать со страницей, до того как она загрузится на 100%
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options,
                              service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))

    print("Start test")

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

    driver.quit()

    print("Finish test")