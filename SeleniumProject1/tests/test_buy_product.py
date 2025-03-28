from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


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

    print("Finish test")