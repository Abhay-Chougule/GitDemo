from selenium.webdriver.common.by import By


class ConfirmPage:

    nameCountry = (By.ID, "country")
    selectcountry = (By.XPATH, "//a[text()='India']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    def __init__(self, driver):
        self.driver = driver

    def countryEnter(self):
        return self.driver.find_element(*ConfirmPage.nameCountry)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectcountry)

    def purchaseItem(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def alertMessage(self):
        return self.driver.find_element(*ConfirmPage.alert)