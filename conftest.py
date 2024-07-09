import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield driver
    driver.close()