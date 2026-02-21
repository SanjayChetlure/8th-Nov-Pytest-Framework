from selenium.webdriver.common.by import By

#POM class2
class SwagLabHomePage:

    # 1: declare locator globally
    header="//div[@class='app_logo']"


    # 2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver


    # 3: perform actions
    def getHeaderName(self):
        actHeader=self.driver.find_element(By.XPATH,self.header).text
        return actHeader