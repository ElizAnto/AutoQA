import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get Current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL: " + get_url)

    """Method Assert Word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f".//Screen//{name_screenshot}")

    """Method Assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method city is active"""

    def city_is_active(self, city_active, name_city):
        name_city_active = city_active.text
        if name_city_active == name_city:
            print("City active")
            return 1
        else:
            print("City is not active")
            return 0

    """Method equality"""

    def equality(self, one, two):
        one_value = one.text
        two_value = two.text
        assert one_value == two_value
        print("Good equality")