import time
from turtle import isvisible
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *
from functions.helpers import Helpfunc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class TestSearch(Helpfunc):
    def test_detailed_movie_review(self):
        searchbars = self.searchbar()
        searchbars.send_keys(test_detailed_searchbar_entry)
        search_result_movie_title = self.waitForElementVisible((By.XPATH,search_result_movie_title_xpath))
        search_result_movie_title.click()
        self.driver.save_screenshot(test_detailed_screenshot)

    def test_evaluation_and_commenting(self):
        main_sign_in_button = self.waitForElementVisible((By.XPATH,main_sign_in_button_xpath))
        main_sign_in_button.click()
        self.driver.save_screenshot(test_evaluation_screenshot)
        sign_in_IMDb = self.waitForElementVisible((By.XPATH,sign_in_IMDb_xpath))
        sign_in_IMDb.click()
        self.driver.save_screenshot(sign_in_IMDb_screenshot)
        email_phone_text = self.waitForElementVisible((By.XPATH,email_phone_text_xpath))
        assert email_phone_text.text == email_phone_assert_text
        email_data_input = self.waitForElementVisible((By.XPATH,email_data_input_xpath))
        email_data_input.send_keys(email_data_input_entry)
        password_input = self.waitForElementVisible((By.XPATH,password_input_xpath))
        password_input.send_keys(password_data_input)
        sign_in_button = self.waitForElementVisible((By.XPATH,sign_in_button_xpath))
        sign_in_button.click()
        searchbars = self.searchbar()
        searchbars.send_keys(test_evaluation_searchbar_entry)
        search_result_movie_title = self.waitForElementVisible((By.XPATH, search_result_movie_title_xpath))
        search_result_movie_title.click()
        user_review_button = self.waitForElementVisible((By.XPATH,user_review_button_xpath))
        user_review_button.click()
        review_this_title_button = self.waitForElementVisible((By.XPATH,review_this_title_button_xpath))
        review_this_title_button.click()
        self.driver.save_screenshot(test_commenting_screenshot)
        time.sleep(3)
        rating_select = self.waitForElementVisible((By.XPATH,rating_select_xpath))
        rating_select.click()
        write_review_title = self.waitForElementVisible((By.XPATH,write_review_title_xpath))
        write_review_title.send_keys(write_review_title_entry)
        write_review_comment= self.waitForElementVisible((By.XPATH,write_review_comment_xpath))
        write_review_comment.send_keys(write_review_comment_entry)
        select_spoiler_preference = self.waitForElementVisible((By.XPATH,select_spoiler_preference_xpath)) 
        select_spoiler_preference.click()
        review_submit_button = self.waitForElementVisible((By.XPATH,review_submit_button_xpath))
        review_submit_button.click()
        submit_message = self.waitForElementVisible((By.XPATH,submit_message_xpath))
        assert submit_message.text == submit_message_assert_text
        self.driver.save_screenshot(test_evaluation_commenting_screenshot)
        
    
        


        

            
