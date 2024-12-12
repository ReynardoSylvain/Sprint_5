import pytest
from selenium import webdriver
from urls import URLS

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(URLS.homepage)
    yield browser
    browser.quit()
