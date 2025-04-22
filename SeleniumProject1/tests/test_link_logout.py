import os

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.description("Test link about")
def test_link_about():
    """Дымовое тестирование кнопки Logout"""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Режим инкогнито, убирает окно об утечке пароля
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        options=options,
        service=Service(os.path.join("..", "resource", "chromedriver.exe"))
    )

    print("Start test")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_menu_logout()

    print("Finish test")

    driver.quit()
