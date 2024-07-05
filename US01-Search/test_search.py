import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *
from functions.helpers import Helpfunc


@pytest.mark.usefixtures("setup")
class TestSearch(Helpfunc):

    def test_movie_search(self):
        searchbars = self.searchbar()
        searchbars.send_keys(Movie_Search_XPATH)
        self.driver.save_screenshot(Movie_Search_Name_Screenshot)
        search_result_movie_name = self.waitForElementVisible((By.XPATH, Search_Result_Movie_Name_XPATH))
        search_result_movie_name .click()
        self.driver.save_screenshot(Movie_Search_Detail_Screenshot)

    def test_director_name(self):
        searchbars = self.searchbar()
        searchbars.send_keys(Director_Name_Search_XPATH)
        search_result_director_name = self.waitForElementVisible((By.XPATH,Director_Name_Result_XPATH))
        search_result_director_name.click()
        self.driver.save_screenshot(Director_Name_Screenshot)

    def test_actor_name(self):
        searchbars = self.searchbar()
        searchbars.send_keys(Actor_Search_XPATH)
        search_result_actor_name = self.waitForElementVisible((By.XPATH,Search_Result_Actor_Name_XPATH))
        search_result_actor_name.click()
        self.driver.save_screenshot(Actor_Name_Screenshot)
