from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_link_about():
    driver = webdriver.Chrome(options=webdriver.ChromeOptions(),
                              service=Service('C:\\Users\\Toughie\\PycharmProjects\\resource\\chromedriver.exe'))

    print("Start test")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_menu_about()

    print("Finish test")