from selenium.webdriver.common.by import By

from PageObjectModel.ConfirmPage import ConfirmPage


class CheckoutPage:

    cards = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    cart = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

    def cartCheckout(self):
        return self.driver.find_element(*CheckoutPage.cart)


