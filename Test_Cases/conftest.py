import pytest
from selenium import webdriver

from UtilityClasses.readProperties import ReadConfig

def openApp(driver):
    driver.get(ReadConfig.getAppCred("App Credentials", "url"))
    driver.maximize_window()
    driver.implicitly_wait(5)


@pytest.fixture
def initializeBrowser(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        openApp(driver)
        return driver
    elif browser=="firefox":
        driver = webdriver.Firefox()
        openApp(driver)
        return driver
    elif browser=="edge":
        driver=webdriver.Edge()
        openApp(driver)
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser",
                    action="store",
                    default="firefox")

@pytest.fixture()
def browser(request):
  return request.config.getoption("--browser")





