import time

import pytest
from selenium import webdriver
from Page_Classes.HomePage import SwagLabHomePage
from Page_Classes.LoginPage import SwagLabLoginPage
from UtilityClasses.customLogger import LogGen
from UtilityClasses.readProperties import ReadConfig
from UtilityClasses.screenshotUtility import ScreenshotUtility


class Test_SwagLabLogin:

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_TC1_loginWithValidData(self,initializeBrowser,request):
        driver=initializeBrowser
        login = SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppCred("App Credentials","username"))
        self.logger.info("--username entered--")
        time.sleep(1)
        login.enterPassword(ReadConfig.getAppCred("App Credentials","password"))
        self.logger.info("--password entered--")
        time.sleep(1)
        login.clickOnLoginBtn()
        self.logger.info("--clicked on login button--")

        home = SwagLabHomePage(driver)
        actHederName = home.getHeaderName()
        expHeaderName = "Swag Labs"

        if actHederName == expHeaderName:
            self.logger.info("--act & Exp header name matched--")
            assert True
        else:
            self.logger.info("--act & Exp header name mis-matched--")
            #ScreenshotUtility.captureSS(driver,"test_TC1_loginWithValidData")
            ScreenshotUtility.captureSS(driver,request.node.name)
            assert False
        time.sleep(10)

    @pytest.mark.smoke
    def test_TC2_loginWithInvalidData(self,initializeBrowser,request):
        driver=initializeBrowser
        login = SwagLabLoginPage(driver)
        login.enterUsername("standard_user")
        self.logger.info("--username entered--")
        time.sleep(1)
        login.enterPassword("abcd")
        self.logger.info("--password entered--")
        time.sleep(1)
        login.clickOnLoginBtn()
        self.logger.info("--clicked on login btn--")
        time.sleep(2)
        actErrorMsg = login.getLoginFailedErrorMsg()
        expErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        print("act Error: ", actErrorMsg)
        print("Exp Error: ", expErrorMsg)

        if actErrorMsg == expErrorMsg:
            self.logger.info("--act & exp login failed error msg matched--")
            assert True
        else:
            ScreenshotUtility.captureSS(driver, request.node.name)
            self.logger.info("--act & exp login failed error msg matched--")
            assert False
        time.sleep(5)

    @pytest.mark.functional
    @pytest.mark.regression
    def test_TC3_loginWithInvalidData(self, initializeBrowser, request):
        driver = initializeBrowser
        login = SwagLabLoginPage(driver)
        login.enterUsername("standard_user")
        self.logger.info("--username entered--")
        time.sleep(1)
        login.enterPassword("abcd")
        self.logger.info("--password entered--")
        time.sleep(1)
        login.clickOnLoginBtn()
        self.logger.info("--clicked on login btn--")
        time.sleep(2)
        actErrorMsg = login.getLoginFailedErrorMsg()
        expErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        print("act Error: ", actErrorMsg)
        print("Exp Error: ", expErrorMsg)

        if actErrorMsg == expErrorMsg:
            self.logger.info("--act & exp login failed error msg matched--")
            assert True
        else:
            ScreenshotUtility.captureSS(driver, request.node.name)
            self.logger.info("--act & exp login failed error msg matched--")
            assert False
        time.sleep(5)


