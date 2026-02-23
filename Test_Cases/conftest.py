import pytest
from selenium import webdriver

@pytest.fixture
def initializeBrowser():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver