import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.globalConstants import *


class Helpfunc:
    def waitForElementVisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def searchbar(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH,"/html//input[@id='suggestion-search']")))
    
    def sign_in_edit_delete(self, timeout = 10):
        main_sign_in_button = self.waitForElementVisible((By.XPATH,main_sign_in_button_xpath))
        main_sign_in_button.click()
        self.driver.save_screenshot(delete_comment_screenshot)
        sign_in_IMDb = self.waitForElementVisible((By.XPATH,sign_in_IMDb_xpath))
        sign_in_IMDb.click()
        self.driver.save_screenshot(delete_comment_sign_in_screenshot)
        email_phone_text = self.waitForElementVisible((By.XPATH,email_phone_text_xpath))
        assert email_phone_text.text == email_phone_assert_text
        email_data_input = self.waitForElementVisible((By.XPATH,email_data_input_xpath))
        email_data_input.send_keys(email_data_input_entry)
        password_input = self.waitForElementVisible((By.XPATH,password_input_xpath))
        password_input.send_keys(password_input_entry)
        sign_in_button = self.waitForElementVisible((By.XPATH,sign_in_button_xpath))
        sign_in_button.click()
        searchbars = self.searchbar()
        searchbars.send_keys(delete_comment_searchbar_entry)
        search_result_movie_title = self.waitForElementVisible((By.XPATH, search_result_movie_title_xpath))
        search_result_movie_title.click()
        user_review_button = self.waitForElementVisible((By.XPATH,user_review_button_xpath))
        user_review_button.click()
        sort_by = self.waitForElementVisible((By.CSS_SELECTOR,sort_by_css))
        sort_by.click()
        self.driver.save_screenshot(delete_comment_check_screenshots)
        point_button = self.waitForElementVisible((By.XPATH,point_button_xpath))
        point_button.click()


