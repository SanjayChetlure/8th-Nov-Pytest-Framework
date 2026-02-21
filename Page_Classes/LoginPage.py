from selenium.webdriver.common.by import By


#pom class/ page class / screen class
class SwagLabLoginPage:

    #1: declare locator globally
    username="//input[@name='user-name']"
    password="//input[@name='password']"
    login="//input[@name='login-button']"
    errorMsg="//h3[contains(text(),'Username and password do not match')]"


    #2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver        #classVariabel=localVariable


    #3: perform actions
    def enterUsername(self,UnValue):
        self.driver.find_element(By.XPATH,self.username).send_keys(UnValue)

    def enterPassword(self,pwdValue):
        self.driver.find_element(By.XPATH,self.password).send_keys(pwdValue)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH,self.login).click()

    def getLoginFailedErrorMsg(self):
        actErrorMSg=self.driver.find_element(By.XPATH,self.errorMsg).text
        return actErrorMSg