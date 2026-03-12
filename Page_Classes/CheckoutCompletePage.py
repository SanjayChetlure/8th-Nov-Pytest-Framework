from selenium.webdriver.common.by import By

#POM class2
class SwagLabCheckoutCompletePage:

    # 1: declare locator globally
    orderComplete="//h2[@class='complete-header']"


    # 2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver


    # 3: perform actions
    def getOrderCompleteMsg(self):
        msg=self.driver.find_element(By.XPATH,self.orderComplete).text
        return msg
