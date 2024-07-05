import time
from turtle import isvisible
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *
from functions.helpers import Helpfunc


@pytest.mark.usefixtures("setup")
class TestSearch(Helpfunc):

    def test_comment_check(self):
        searchbars = self.searchbar()
        searchbars.send_keys(test_comment_searchbar_entry)
        search_result_movie_title = self.waitForElementVisible((By.XPATH, search_result_movie_title_xpath))
        search_result_movie_title.click()
        user_review_button = self.waitForElementVisible((By.XPATH,user_review_button_xpath))
        user_review_button.click()
        sort_by = self.waitForElementVisible((By.CSS_SELECTOR,sort_by_css))
        sort_by.click()
        self.driver.save_screenshot(test_comment_check_screenshot)