from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

class LoginPage(Base):
    """Вход в систему под пользовательскими данными"""

    # Locators

    input_button = "//a[@title='Вход в Личный кабинет']"
    login = "//input[@name='login']"
    password = "//input[@name='password']"
    remember_checkbox = "//span[@class='ui-checkboxradio-icon ui-corner-all ui-icon ui-icon-background ui-icon-check ui-state-checked ui-state-hover']"
    login_button = "//input[@value='Вход']"
    main_word = "//a[@title='Каталог товаров']"

    # Getters

    def get_input_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_button)))

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_remember_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remember_checkbox)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_input_button(self):
        self.get_input_button().click()
        print("Click input button")

    def input_login(self, login):
        self.get_login().send_keys(login)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_remember_checkbox(self):
        self.get_remember_checkbox().click()
        print("Click remember checkbox")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def authorisation(self):
        Logger.add_start_step(method="authorisation")
        self.get_current_url()
        self.click_input_button()
        self.input_login("test@testov.ru")
        self.input_password("Onl1netr")
        self.click_remember_checkbox()
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Каталог")
        Logger.add_end_step(url=self.driver.current_url, method="authorisation")