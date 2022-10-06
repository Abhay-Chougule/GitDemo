import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='India']")))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("utilities/logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger


