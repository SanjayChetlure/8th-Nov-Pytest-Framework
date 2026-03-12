from selenium.webdriver.common.by import By

#POM class2
class SwagLabHomePage:

    # 1: declare locator globally
    header="//div[@class='app_logo']"
    backpackProduct="(//div[@class='inventory_item_name '])[1]"
    allProductsXpath="//div[@class='inventory_item_label']//a//div"
    backpackProductPrice="(//div[@class='inventory_item_price'])[1]"
    allProductPrice="//div[@class='inventory_item_price']"
    addToCart1stProduct="//button[@id='add-to-cart-sauce-labs-backpack']"
    cartLink="//a[@class='shopping_cart_link']"


    # 2: initialization of webdriver object within constructor
    def __init__(self,driver):
        self.driver=driver


    # 3: perform actions
    def getHeaderName(self):
        actHeader=self.driver.find_element(By.XPATH,self.header).text
        return actHeader

    def get1stProductName(self):
        firstProductName=self.driver.find_element(By.XPATH,self.backpackProduct).text
        return firstProductName

    def getAllProductSize(self):
        allProducts=self.driver.find_elements(By.XPATH,self.allProductsXpath)
        totalElementsSize=len(allProducts)
        return totalElementsSize

    def get1stProductPrice(self):
        firstProductPrice=self.driver.find_element(By.XPATH,self.backpackProductPrice).text
        firstProductPrice=firstProductPrice[1:]
        return firstProductPrice

    def getAllProductPrice(self):
        allProductsPriceAddress=self.driver.find_elements(By.XPATH,self.allProductPrice)
        totalPrice=0     #39.98
        for singlePriceAddress in allProductsPriceAddress:
            s1=singlePriceAddress.text     #$29.99
            s1=s1[1:]                      #29.99       ->str
            s1=float(s1)                   #29.99       ->float
            totalPrice=totalPrice+s1       #29.99 + 9.99 = 39.98
        return totalPrice

    def click1stProductAddToCart(self):
        self.driver.find_element(By.XPATH,self.addToCart1stProduct).click()

    def clickOnCartLink(self):
        self.driver.find_element(By.XPATH,self.cartLink).click()
