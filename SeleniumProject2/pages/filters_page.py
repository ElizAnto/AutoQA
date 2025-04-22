import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

class SmartFiltersPage(Base):
    """Выбор необходимых фильтров"""

    # Locators

        # Наличие
    stock_in_stock = "//label[@id='l5950a4a1de00bc24202c5f78a0a726be']"
        # Скидки
    discount_in_action = "//label[@id='lebb67a4271abe715344471b0f16321f6']"
        # Производитель
    manufacturer_xiaomi = "//label[@id='l46435b29b8bf4dd5d73b4a4fa25f3e50']"
        # Цена
    price_menu = "//div[@title='Подобрать по цене в категории «Смартфоны»']"
    price_min = "//input[@id='price1']"
    price_max = "//input[@id='price2']"
        # Подбор по рейтингу
    score_menu = "//div[@title='Подбор по рейтингу в категории «Смартфоны»']"
    score_5 = "//label[@id='lf7c90596d2b3675b0f1cd96316dc4245']"
        # Операционная система
    os_menu = "//div[@title='Операционная система в категории «Смартфоны»']"
    os_android_14 = "//label[@id='l7c92cc9fcdef7b050c95a2e91aee68db']"
        # Платформа
    platform_hyperos = "//label[@id='l31beebb822a6bf5402fb395a273978d5']"
        # Встроенная память
    memory_rom_128 = "//label[@id='l77edb32393ed9592a633d06859632e56']"
        # Оперативная память
    memory_ram_8 = "//label[@id='l7240efd2955edd8517f9dfebe08f5261']"
        # Диагональ дисплея
    display_diagonal_min = "//input[@id='diagonal1']"
    display_diagonal_max = "//input[@id='diagonal2']"
        # Цвет
    colour_black = "//label[@id='lf7db97e847b201c1a4f0627f817f3b72']"

    select_button = "//a[@title='Подобрать']"
    main_word = "//a[@class='indexGoods__item__name  ']"

    # Getters

    def get_stock_in_stock(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stock_in_stock)))

    def get_discount_in_action(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount_in_action)))

    def get_manufacturer_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer_xiaomi)))

    def get_price_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_menu)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_score_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.score_menu)))

    def get_score_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.score_5)))

    def get_os_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.os_menu)))

    def get_os_android_14(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.os_android_14)))

    def get_platform_hyperos(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.platform_hyperos)))

    def get_memory_rom_128(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory_rom_128)))

    def get_memory_ram_8(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory_ram_8)))

    def get_display_diagonal_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.display_diagonal_min)))

    def get_display_diagonal_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.display_diagonal_max)))

    def get_colour_black(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.colour_black)))

    def get_select_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_stock_in_stock(self):
        self.get_stock_in_stock().click()
        print("Click stock in stock")

    def click_discount_in_action(self):
        self.get_discount_in_action().click()
        print("Click discount in action")

    def click_manufacturer_xiaomi(self):
        self.get_manufacturer_xiaomi().click()
        print("Click manufacturer xiaomi")

    def click_price_menu(self):
        self.get_price_menu().click()
        print("Click price menu")

    def clear_price_min(self):
        self.get_price_min().send_keys(Keys.CONTROL + "a")
        self.get_price_min().send_keys(Keys.DELETE)
        print("Clear price min")

    def input_price_min(self, price):
        self.get_price_min().send_keys(price)
        print("Input price min " + price)

    def clear_price_max(self):
        self.get_price_max().send_keys(Keys.CONTROL + "a")
        self.get_price_max().send_keys(Keys.DELETE)
        print("Clear price max")

    def input_price_max(self, price):
        self.get_price_max().send_keys(price)
        print("Input price max " + price)

    def click_score_menu(self):
        self.get_score_menu().click()
        print("Click score menu")

    def click_score_5(self):
        self.get_score_5().click()
        print("Click score 5")

    def click_os_menu(self):
        self.get_os_menu().click()
        print("Click os menu")

    def click_os_android_14(self):
        self.get_os_android_14().click()
        print("Click os android 14")

    def click_platform_hyperos(self):
        self.get_platform_hyperos().click()
        print("Click platform hyperos")

    def click_memory_rom_128(self):
        self.get_memory_rom_128().click()
        print("Click memory rom 128")

    def click_memory_ram_8(self):
        self.get_memory_ram_8().click()
        print("Click memory ram 8")

    def clear_display_diagonal_min(self):
        self.get_display_diagonal_min().send_keys(Keys.CONTROL + "a")
        self.get_display_diagonal_min().send_keys(Keys.DELETE)
        print("Clear display diagonal min")

    def input_display_diagonal_min(self, value):
        self.get_display_diagonal_min().send_keys(value)
        print("Input display diagonal min " + value)

    def clear_display_diagonal_max(self):
        self.get_display_diagonal_max().send_keys(Keys.CONTROL + "a")
        self.get_display_diagonal_max().send_keys(Keys.DELETE)
        print("Clear display diagonal max")

    def input_display_diagonal_max(self, value):
        self.get_display_diagonal_max().send_keys(value)
        print("Input display diagonal max " + value)

    def click_colour_black(self):
        self.get_colour_black().click()
        print("Click colour black")

    def click_select_button(self):
        self.get_select_button().click()
        print("Click select button")

    # Methods

    def choose_filters(self):
        Logger.add_start_step(method="choose_filters")
        self.get_current_url()
        self.click_stock_in_stock()
        self.click_discount_in_action()
        self.click_manufacturer_xiaomi()
        self.click_price_menu()
        self.clear_price_min()
        self.input_price_min("10000")
        self.clear_price_max()
        self.input_price_max("60000")
        self.click_score_menu()
        self.click_score_5()
        self.click_os_android_14()
        self.click_platform_hyperos()
        self.click_memory_rom_128()
        self.click_memory_ram_8()
        self.clear_display_diagonal_min()
        self.input_display_diagonal_min("6")
        self.clear_display_diagonal_max()
        self.input_display_diagonal_max("6.7")
        self.click_colour_black()
        time.sleep(0.5) # Без задержки цвет не успевает установиться
        self.click_select_button()
        self.assert_word(self.get_main_word(), "Xiaomi Redmi Note 14 8/128GB Черный")
        Logger.add_end_step(url=self.driver.current_url, method="choose_filters")