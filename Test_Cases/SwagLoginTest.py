import time
from selenium import webdriver
from Page_Classes.HomePage import SwagLabHomePage
from Page_Classes.LoginPage import SwagLabLoginPage
from UtilityClasses.readProperties import ReadConfig


class Test_SwagLabLogin:

    def test_TC1_loginWithValidData(self,initializeBrowser):
        driver=initializeBrowser
        login = SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppCred("App Credentials","username"))
        time.sleep(1)
        login.enterPassword(ReadConfig.getAppCred("App Credentials","password"))
        time.sleep(1)
        login.clickOnLoginBtn()

        home = SwagLabHomePage(driver)
        actHederName = home.getHeaderName()
        expHeaderName = "Swag Labs"

        if actHederName == expHeaderName:
            assert True
        else:
            assert False
        time.sleep(10)

    def test_TC2_loginWithInvalidData(self,initializeBrowser):
        driver=initializeBrowser
        login = SwagLabLoginPage(driver)
        login.enterUsername("standard_user")
        time.sleep(1)
        login.enterPassword("abcd")
        time.sleep(1)
        login.clickOnLoginBtn()
        time.sleep(2)
        actErrorMsg = login.getLoginFailedErrorMsg()
        expErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        print("act Error: ", actErrorMsg)
        print("Exp Error: ", expErrorMsg)

        if actErrorMsg == expErrorMsg:
            assert True
        else:
            assert False
        time.sleep(5)



