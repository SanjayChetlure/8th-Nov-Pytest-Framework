from selenium.webdriver.common.by import By

#POM class2
class SwagLabYourCartPage:

    # 1: declare locator globally
    checkoutBtn="//button[text()='Checkout']"


    # 2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver


    # 3: perform actions
    def clickOnCheckoutBtn(self):
        self.driver.find_element(By.XPATH,self.checkoutBtn).click()
