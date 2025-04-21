from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class SmartPage(Base):
    """Переход в категорию Смартфоны"""

    # Locators

    catalog = "//a[@title='Каталог товаров']"
    smartphone = "//a[@title='Перейти в категорию «Смартфоны»']"
    main_word = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_smartphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphone)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print("Click catalog")

    def click_smartphone(self):
        self.get_smartphone().click()
        print("Click smartphone")

    # Methods

    def search_smart(self):
        self.get_current_url()
        self.click_catalog()
        self.click_smartphone()
        self.assert_word(self.get_main_word(), "Смартфоны")


