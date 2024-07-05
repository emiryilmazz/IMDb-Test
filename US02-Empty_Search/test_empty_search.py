import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *
from functions.helpers import Helpfunc


@pytest.mark.usefixtures("setup")
class TestSearch(Helpfunc):

    def test_empty_search(self):
        searchButton = self.waitForElementVisible((By.XPATH,Empty_Search_XPATH))
        searchButton.click()
        empty_search_text=self.waitForElementVisible((By.XPATH,Empty_Search_Text_XPATH))
        assert empty_search_text.text == Empty_Search_Text_Assert
        self.driver.save_screenshot(Empty_Search_Screenshot)                                      