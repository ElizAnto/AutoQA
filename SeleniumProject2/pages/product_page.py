from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ProductPage(Base):
    """Выбор продукта и отправка в корзину"""

    # Locators

    product="//a[@class='indexGoods__item__name  ']"
    phone_word = "//h1[@itemprop='name']"
    buy_button = "(//a[@data-handler='buy'])[1]"
    order_button = "//a[@id='js__popup_addedToCart__cartLinkID']"
    main_word = "//a[@data-popupcaption='Поделиться корзиной']"

    # Getters

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_phone_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_word)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_product(self):
        self.get_product().click()
        print("Click product")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click buy button")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_product()
        self.assert_word(self.get_phone_word(), "Смартфон Xiaomi Redmi Note 14 8/128GB Черный")
        self.click_buy_button()
        self.click_order_button()
        self.assert_word(self.get_main_word(), "Ссылка на вашу корзину")
