import pytest

"""Для всех тестов"""
@pytest.fixture()
def set_up():
    # Driver, URL, get(URL), maximize
    print("Start test")
    yield
    # driver.quit()
    print("Finish test")

"""Для группы тестов"""
@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")