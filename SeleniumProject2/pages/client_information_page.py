from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ClientInformationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    name = "//input[@title='Контактное лицо']"
    phone = "//input[@id='cellphone__ID']"
    sms_time = "//select[@id='sms_time__ID']"
    sms_time_2 = "//option[@value='2']"
    main_word = "//div[@class='note note__dash gray']" # Ваш Заказ будет обработан автоматически, о готовности заказа к получению мы уведомим Вас по SMS и e-mail.

    # Getters

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_sms_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sms_time)))

    def get_sms_time_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sms_time_2)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def clear_name(self):
        self.get_name().send_keys(Keys.CONTROL + "a")
        self.get_name().send_keys(Keys.DELETE)
        print("Clear name")

    def input_name(self, value):
        self.get_name().send_keys(value)
        print("Input name " + value)

    def clear_phone(self):
        self.get_phone().send_keys(Keys.CONTROL + "a")
        self.get_phone().send_keys(Keys.DELETE)
        print("Clear phone")

    def input_phone(self, value):
        self.get_phone().send_keys(value)
        print("Input phone " + value)

    def click_sms_time(self):
        self.get_sms_time().click()
        print("Click sms time")

    def click_sms_time_2(self):
        self.get_sms_time_2().click()
        print("Click sms time 2")

    # Methods

    def input_information(self):
        self.get_current_url()
        self.clear_name()
        self.input_name("Антон Елизаров")
        self.clear_phone()
        self.input_phone("+7987654321")
        self.click_sms_time()
        self.click_sms_time_2()
        self.assert_word(self.get_main_word(), "Ваш Заказ будет обработан автоматически, о готовности заказа к получению мы уведомим Вас по SMS и e-mail.")

