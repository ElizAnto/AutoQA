from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ClearCartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart = "//a[@class='huab__cell__link header__basket__color0 js__header__basketLink']"
    clear_button = "//a[@title='Очистить корзину']"
    clear_confirm_button = "//a[@title='Удалить товары из корзины']"
    main_word = "//span[@class='multicart__header__itemName']"

    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_button)))

    def get_clear_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_confirm_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

        # Actions

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_clear_button(self):
        self.get_clear_button().click()
        print("Click clear_button")

    def click_clear_confirm_button(self):
        self.get_clear_confirm_button().click()
        print("Click clear confirm button")

    # Methods

    def clear_cart(self):
        self.get_current_url()
        self.click_cart()
        self.click_clear_button()
        self.click_clear_confirm_button()
        self.assert_word(self.get_main_word(), "Основная")