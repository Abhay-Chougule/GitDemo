from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModel.CheckoutPage import CheckoutPage


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    alerts = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def clickCheckbox(self):
        return self.driver.find_element(*HomePage.name)

    def getGender(self):
        return self.driver.find_element(By.ID, "exampleFormControlSelect1")


    def submitForm(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alerts)

