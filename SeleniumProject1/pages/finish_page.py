from base.base_class import Base

class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver) # Указатель, что это потомок класса Base
        self.driver = driver

    # Locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.get_screenshot()