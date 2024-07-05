from selenium import webdriver
from constants.globalConstants import *
import pytest

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()