from selenium.webdriver.common.by import By

#POM class2
class SwagLabCheckoutOverviewPage:

    # 1: declare locator globally
    finish="//button[text()='Finish']"


    # 2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver


    # 3: perform actions
    def clickOnFinishBtn(self):
        self.driver.find_element(By.XPATH,self.finish).click()
