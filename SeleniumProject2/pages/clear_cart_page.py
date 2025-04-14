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
    city_active = "//span[@class='active']"
    city_close = "(//a[@title='Закрыть окно'])[2]"
    city_name = "Самара"
    city_samara = "//a[@title='" + city_name + "']"
        # Пункты выдачи
    delivery_word = "//h2[@class='floatLeft']"
    point_may = "//label[@for='shipmentradio392']" # ТЦ Май
        # Способы оплаты
    cash = "//label[@for='paymentradio1']"
        # Оформление
    order_button = "//input[@class='button button__orange semibold js__formBoxMainButton floatRight']"
    main_word = "//label[@for='delivery_date']"

    # Getters

    def get_cost_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cost_product)))

    def get_cost_final(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cost_final)))

    def get_city_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_menu)))

    def get_city_active(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_active)))

    def get_city_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_close)))

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
        print("Click cost final")

    def click_city_menu(self):
        self.get_city_menu().click()
        print("Click city menu")

    def click_city_close(self):
        self.get_city_close().click()
        print("Click city close")

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
        self.equality(self.get_cost_product(), self.get_cost_final())
        self.click_city_menu()
        # Проверяем активен ли город и получаем результат (1 или 0)
        city_active_status = self.city_is_active(self.get_city_active(), self.city_name)
        # Если город не активен (вернулся 0), тогда кликаем для выбора города
        if not city_active_status:
            self.click_city_samara()
        else:
            self.click_city_close()
        self.assert_word(self.get_delivery_word(), "Пункты выдачи в Самаре")
        self.click_point_may()
        self.click_cash()
        self.click_order_button()
        self.assert_word(self.get_main_word(), "Желаемая дата получения заказа")

