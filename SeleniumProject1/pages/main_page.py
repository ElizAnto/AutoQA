import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

class MainPage(Base):
    """Главная страница"""
    def __init__(self, driver):
        super().__init__(driver) # Указатель, что это потомок класса Base
        self.driver = driver

    # Locators

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//a[@class='shopping_cart_link']"
    menu = "//button[@id='react-burger-menu-btn']"
    link_logout = "//a[@id='logout_sidebar_link']"

    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_logout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_logout)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product_1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product_2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select product_3")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click menu")

    def click_link_logout(self):
        self.get_link_logout().click()
        print("Click link logout")

    # Methods

    """Добавление товаров в корзину"""

    def select_products_1(self):
        """sauce-labs-backpack"""
        with allure.step("Select products 1"):
            Logger.add_start_step(method="select_products_1")
            self.get_current_url()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method="select_products_1")

    def select_products_2(self):
        """sauce-labs-bike-light"""
        Logger.add_start_step(method="select_products_2")
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="select_products_2")

    def select_products_3(self):
        """sauce-labs-bolt-t-shirt"""
        Logger.add_start_step(method="select_products_3")
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="select_products_3")

    """Кнопка меню"""

    def select_menu_logout(self):
        """Logout"""
        with allure.step("Select menu logout"):
            Logger.add_start_step(method="select_menu_logout")
            self.get_current_url()
            self.click_menu()
            self.click_link_logout()
            self.assert_url("https://www.saucedemo.com/")
            Logger.add_end_step(url=self.driver.current_url, method="select_menu_logout")
