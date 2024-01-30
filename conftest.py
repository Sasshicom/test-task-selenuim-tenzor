from selenium import webdriver
import pytest
import os


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    working_directory = os.getcwd()

    # Определяем опшенсы хрома для того, чтобы можно было выкачивать файлик в нужную себе директорию
    # и игнорировать ошибку непроверенного файла при скачивании
    prefs = {"download.default_directory": working_directory,
             'safebrowsing.enabled': True}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.maximize_window()
    return browser
