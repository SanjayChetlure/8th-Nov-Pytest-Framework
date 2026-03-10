import time

import pytest
from selenium import webdriver
from Page_Classes.HomePage import SwagLabHomePage
from Page_Classes.LoginPage import SwagLabLoginPage
from UtilityClasses.customLogger import LogGen
from UtilityClasses.readExcel import ReadExcel
from UtilityClasses.readProperties import ReadConfig
from UtilityClasses.screenshotUtility import ScreenshotUtility


class Test_SwagLabLogin:

    logger=LogGen.loggen()

    def loginToApp(self,driver):
        login = SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppCred("App Credentials", "username"))
        self.logger.info("--username entered--")
        time.sleep(1)
        login.enterPassword(ReadConfig.getAppCred("App Credentials", "password"))
        self.logger.info("--password entered--")
        time.sleep(1)
        login.clickOnLoginBtn()
        self.logger.info("--clicked on login button--")

    @pytest.mark.sanity
    def test_TC1_loginWithValidData(self,initializeBrowser,request):
        driver=initializeBrowser

        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        actHederName = home.getHeaderName()
        expHeaderName = ReadExcel.getExcelData(1,1)

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
        expErrorMsg =  ReadExcel.getExcelData(2,1)  #"Epic sadface: Username and password do not match any user in this service"

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


    def test_TC3_verifyProductName(self, initializeBrowser, request):
        driver = initializeBrowser

        self.loginToApp(driver)

        home=SwagLabHomePage(driver)
        actProductName=home.get1stProductName()
        expProductName="Sauce Labs Backpack"      #ReadExcel.getExcelData(3,1)
        print(actProductName)
        print(expProductName)
        if actProductName == expProductName:
            self.logger.info("--act & exp product name matched--")
            assert True
        else:
            ScreenshotUtility.captureSS(driver, request.node.name)
            self.logger.info("--act & exp product name msg matched--")
            assert False


    def test_TC4_verifyProductSize(self, initializeBrowser, request):
        driver = initializeBrowser
        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        time.sleep(4)
        actProductSize = home.getAllProductSize()
        expProductSize = 6   #ReadExcel.getExcelData(4,1)
        print(actProductSize)
        print(expProductSize)
        if actProductSize == expProductSize:
            self.logger.info("--act & exp product size matched--")
            assert True
        else:
            ScreenshotUtility.captureSS(driver, request.node.name)
            self.logger.info("--act & exp product size msg matched--")
            assert False

    @pytest.mark.productModule
    def test_TC5_verifyProductPrice(self, initializeBrowser, request):
        driver = initializeBrowser
        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        time.sleep(4)
        actProductPrice = float(home.get1stProductPrice())
        expProductPrice = 29.99  # ReadExcel.getExcelData(5,1)
        print(actProductPrice)
        print(expProductPrice)
        if actProductPrice == expProductPrice:
            self.logger.info("--act & exp product price matched--")
            assert True
        else:
            ScreenshotUtility.captureSS(driver, request.node.name)
            self.logger.info("--act & exp product price msg matched--")
            assert False
