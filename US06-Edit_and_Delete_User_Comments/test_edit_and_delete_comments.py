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

    def test_edit_comment(self):
        sign_in_edit_delete = self.sign_in_edit_delete()
        edit_button = self.waitForElementVisible((By.XPATH,edit_button_xpath))
        edit_button.click()
        time.sleep(4)
        edittitle = self.driver.find_element(By.PARTIAL_LINK_TEXT,edittitle_link_text)
        edittitle.clear()
        edit_title = self.waitForElementVisible((By.CSS_SELECTOR,edit_title_css))
        edit_title.clear()
        edit_title.send_keys(edit_title_entry)
        edit_comment = self.waitForElementVisible((By.XPATH,edit_comment_xpath))
        edit_comment.clear()
        edit_comment.send_keys(edit_comment_entry)
        submit_button = self.waitForElementVisible((By.XPATH,submit_button_xpath))
        submit_button.click()
    
    def test_delete_comment(self):
        sign_in_edit_delete = self.sign_in_edit_delete()
        delete_button = self.waitForElementVisible((By.XPATH,delete_button_xpath))
        delete_button.click()
        delete_item_text = self.waitForElementVisible((By.XPATH,delete_item_text_xpath))
        assert delete_item_text.text == delete_item_assert_text
        confirm_delete_button = self.waitForElementVisible((By.XPATH,confirm_delete_button_xpath))
        confirm_delete_button.click()
