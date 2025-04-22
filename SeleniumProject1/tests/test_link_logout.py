import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.description("Test link about")
def test_link_about(set_up, driver):
    """Дымовое тестирование кнопки Logout"""
    print("Start test")

    login = LoginPage(driver)
    login.authorisation()

    mp = MainPage(driver)
    mp.select_menu_logout()

    print("Finish test")

