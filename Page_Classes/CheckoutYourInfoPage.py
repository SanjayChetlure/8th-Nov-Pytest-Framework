from selenium.webdriver.common.by import By

#POM class2
class SwagLabCheckoutYourInfoPage:

    # 1: declare locator globally
    firstName="//input[@name='firstName']"
    lastName = "//input[@name='lastName']"
    postalCode = "//input[@name='postalCode']"
    continueBtn="//input[@name='continue']"


    # 2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver


    # 3: perform actions
    def enterFirstName(self,FN):
        self.driver.find_element(By.XPATH,self.firstName).send_keys(FN)

    def enterLastName(self, LN):
        self.driver.find_element(By.XPATH, self.lastName).send_keys(LN)

    def enterPostalCode(self, PC):
        self.driver.find_element(By.XPATH, self.postalCode).send_keys(PC)

    def clickOnContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtn).click()
