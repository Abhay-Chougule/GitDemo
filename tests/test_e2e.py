from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjectModel.CheckoutPage import CheckoutPage
from PageObjectModel.ConfirmPage import ConfirmPage
from PageObjectModel.HomePage import HomePage
from TestData.ItemPurchaseData import ItemPurchaseData
from utilities.baseClass import BaseClass


# @pytest.mark.usefixtures("setup")  ## no need , defined baseclass, and used inheritance here

class TestOne(BaseClass):

    def test_e2e(self, getData):
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        cards = checkoutpage.getCardTitles()
        confirmpage = ConfirmPage(self.driver)
        # cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(cardText)
            if cardText == getData["mobileBrand"]:
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.cartCheckout().click()
        confirmpage = checkoutpage.checkOutItems()

        confirmpage.countryEnter().send_keys(getData["Country"])

        self.verifyLinkPresence("India")
        confirmpage.selectCountry().click()
        confirmpage.purchaseItem().click()

        message = confirmpage.alertMessage().text

        assert "Success" in message
        print("Abhay -- changes done in e2e test case -- github")

    @pytest.fixture(params=ItemPurchaseData.test_item_purchase)
    def getData(self, request):
        return request.param

