import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""Для всех тестов"""
@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

"""Для группы тестов"""
@pytest.fixture(scope="function")
def driver():
    print("Initialize driver")
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Режим инкогнито, убирает окно об утечке пароля
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        options=options,
        service=Service(os.path.join("..", "resource", "chromedriver.exe"))
    )
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    driver.maximize_window()

    yield driver

    print("Quit driver")
    driver.quit()