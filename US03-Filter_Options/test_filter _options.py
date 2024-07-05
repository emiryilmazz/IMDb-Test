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

    def test_filter_titles(self):
        all_button = self.waitForElementVisible((By.XPATH,All_Button_XPATH))
        all_button.click()
        select_all_titles = self.waitForElementVisible((By.XPATH,Select_All_Titles_XPATH))
        select_all_titles.click()
        searchbars = self.searchbar()
        searchbars.send_keys(Test_Filter_Searchbar_Entry)
        search_result_movie_title = self.waitForElementVisible((By.XPATH,Search_Result_Movie_Title_XPATH))
        self.driver.save_screenshot(Test_Filter_Titles_Screenshot)

    def test_filter_tv_episode(self):
        all_button = self.waitForElementVisible((By.XPATH,All_Button_XPATH))
        all_button.click()
        select_tv_episode = self.waitForElementVisible((By.XPATH,Select_Tv_Episode_XPATH))
        select_tv_episode.click()
        searchbars = self.searchbar()
        searchbars.send_keys(Tv_Episode_Searchbar_Entry) 
        try:
            tv_episode_dropdownlist = self.waitForElementVisible((By.XPATH,tv_episode_dropdownlist_XPATH))
            assert tv_episode_dropdownlist.text == tv_episode_dropdownlist_text

        except Exception as e:
            self.driver.save_screenshot(Tv_episode_screenshot)
            raise AssertionError(Tv_episode_assertion_error_text + str(e))

    def test_fiter_celebs(self):
        all_button = self.waitForElementVisible((By.XPATH,All_Button_XPATH))
        all_button.click()
        select_celebs = self.waitForElementVisible((By.XPATH,select_celebs_xpath))
        select_celebs.click()
        searchbars = self.searchbar()
        searchbars.send_keys(select_celebs_searchbar_Entry)
        search_result_celebs_title = self.waitForElementVisible((By.XPATH,search_result_celebs_title_xpath)) 
        self.driver.save_screenshot(test_filter_celebs_screenshot)

    def test_filter_compaines(self):
        all_button = self.waitForElementVisible((By.XPATH,All_Button_XPATH))
        all_button.click()
        select_companies = self.waitForElementVisible((By.XPATH,select_companies_xpath))
        select_companies.click()
        searchbars = self.searchbar()
        searchbars.send_keys(select_companies_searchbar_entry)
        try:
            search_result_company_title = self.waitForElementVisible((By.XPATH,search_result_company_title_xpath))
            assert search_result_company_title.text == search_result_company_title_text

        except Exception as e:
            self.driver.save_screenshot(select_companies_screenshot)
            raise AssertionError(select_companies_assertion_text + str(e))
        
    def test_filter_advanced_search(self):
        all_button = self.waitForElementVisible((By.XPATH,All_Button_XPATH))
        all_button.click()
        select_advanced_search = self.waitForElementVisible((By.XPATH,select_advanced_search_xpath))
        select_advanced_search.click()
        page_advanced_search_title = self.waitForElementVisible((By.XPATH,page_advanced_search_title_xpath))
        assert page_advanced_search_title.text == page_advanced_search_title_text
        self.driver.save_screenshot(select_advanced_search_screenshot)
        


        
        
        
    
        
