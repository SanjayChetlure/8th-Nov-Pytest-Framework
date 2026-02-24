import pytest
from selenium import webdriver

from UtilityClasses.readProperties import ReadConfig


@pytest.fixture
def initializeBrowser():
    driver = webdriver.Edge()
    driver.get(ReadConfig.getAppCred("App Credentials","url"))
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver