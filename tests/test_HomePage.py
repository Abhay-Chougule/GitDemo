import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModel.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.baseClass import BaseClass


class TestTwo(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        log.info("test_formSubmission started Executing")
        homepage = HomePage(self.driver)
        log.info("Name used to test is: "+getData["Name"])
        homepage.getName().send_keys(getData["Name"])
        log.info("Email used to test is: " + getData["Email"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.clickCheckbox().click()
        log.info("Gender used to test is: " + getData["Gender"])
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        # time.sleep(2)
        homepage.submitForm().click()

        alertText = homepage.getAlert().text
        print("Abhay-- change done to practice github")

        assert "Success" in alertText
        log.info("refreshing for test with another data")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self, request):
        return request.param

