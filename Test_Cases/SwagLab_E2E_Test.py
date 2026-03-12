import time

import pytest
from selenium import webdriver

from Page_Classes.CheckoutCompletePage import SwagLabCheckoutCompletePage
from Page_Classes.CheckoutOverviewPage import SwagLabCheckoutOverviewPage
from Page_Classes.CheckoutYourInfoPage import SwagLabCheckoutYourInfoPage
from Page_Classes.HomePage import SwagLabHomePage
from Page_Classes.LoginPage import SwagLabLoginPage
from Page_Classes.YourCartPage import SwagLabYourCartPage
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

    def test_TC7_loginWithValidData(self,initializeBrowser,request):
        driver=initializeBrowser

        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        home.click1stProductAddToCart()
        home.clickOnCartLink()
        time.sleep(2)

        yourCart=SwagLabYourCartPage(driver)
        yourCart.clickOnCheckoutBtn()
        time.sleep(2)

        checkoutYourInfo=SwagLabCheckoutYourInfoPage(driver)
        checkoutYourInfo.enterFirstName("abc")  #ReadExcel.getExcelData(7,1)
        checkoutYourInfo.enterLastName("xyz")   #ReadExcel.getExcelData(7,2)
        checkoutYourInfo.enterPostalCode("123") #ReadExcel.getExcelData(7,3)
        checkoutYourInfo.clickOnContinueBtn()
        time.sleep(2)

        CheckoutOverview=SwagLabCheckoutOverviewPage(driver)
        CheckoutOverview.clickOnFinishBtn()
        time.sleep(2)

        checkoutComplete=SwagLabCheckoutCompletePage(driver)
        actOrderCompleteMsg=checkoutComplete.getOrderCompleteMsg()
        expOrderCompleteMsg="Thank you for your order!"   #ReadExcel.getExcelData(7,4)
        if actOrderCompleteMsg == expOrderCompleteMsg:
            self.logger.info("--act & Exp order complete msg matched--")
            assert True
        else:
            self.logger.info("--act & Exp order complete msg mis-matched--")
            ScreenshotUtility.captureSS(driver,request.node.name)
            assert False
        time.sleep(10)

