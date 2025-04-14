from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cost_product = "//b[@class='nowrap']"
    cost_final = "//div[@class='multicart__items__resultsLine__value']"
    city_menu = "//a[@title='Выбрать другой город']"
    city_samara = "//a[@title='Самара']"
        # Пункты выдачи
    delivery_word = "//h2[@class='floatLeft']"
    point_may = "//label[@for='shipmentradio392']" # ТЦ Май
        # Способы оплаты
    cash = "//label[@for='paymentradio1']"
        # Оформление
    order_button = "//input[@class='button button__orange semibold js__formBoxMainButton floatRight']"
    main_word = "(//div[@class='k_centered'])[4]"

    # Getters

    def get_cost_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cost_product)))

    def get_cost_final(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cost_final)))

    def get_city_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_menu)))

    def get_city_samara(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_samara)))

    def get_delivery_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_word)))

    def get_point_may(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.point_may)))

    def get_cash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cash)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_cost_product(self):
        self.get_cost_product().click()
        print("Click cost product")

    def click_cost_final(self):
        self.get_cost_product().click()
        print("Click cost product")

    def click_city_menu(self):
        self.get_city_menu().click()
        print("Click city menu")

    def click_city_samara(self):
        self.get_city_samara().click()
        print("Click city Samara")

    def click_point_may(self):
        self.get_point_may().click()
        print("Click point may")

    def click_cash(self):
        self.get_cash().click()
        print("Click cash")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods

    def product_confirmation(self):
        self.get_current_url()
        self.click_cost_product()
        self.click_cost_final()
        self.click_city_menu()
        self.click_point_may()
        self.assert_word(self.get_delivery_word(), "Пункты выдачи в Самаре")
        self.click_point_may()
        self.click_cash()
        self.click_order_button()
        self.assert_word(self.get_main_word(), "Оформление заказа")

