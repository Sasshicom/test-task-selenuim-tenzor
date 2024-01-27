from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    browser.maximize_window()
    return browser
