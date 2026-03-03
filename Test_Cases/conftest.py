import pytest
from selenium import webdriver

from UtilityClasses.readProperties import ReadConfig

def openApp(driver):
    driver.get(ReadConfig.getAppCred("App Credentials", "url"))
    driver.maximize_window()
    driver.implicitly_wait(5)


@pytest.fixture
def initializeBrowser(browser):
    browser=browser.lower()
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()

    openApp(driver)
    return driver

#below code is to run script on specified browser
def pytest_addoption(parser):
    parser.addoption("--browser",
                    action="store",
                    default="firefox")

@pytest.fixture()
def browser(request):
  return request.config.getoption("--browser")



#below code is to generate html report after execution of every script
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
   metadata['Project Name'] = 'Swag Labs'
   metadata['Module Name'] = 'Login'
   metadata['Tester Name'] = 'Sanjay'




