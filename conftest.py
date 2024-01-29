from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()

    # Определяем опшенсы хрома для того, чтобы можно было выкачивать файлик в нужную себе директорию
    # и игнорировать ошибку непроверенного файла при скачивании
    prefs = {"download.default_directory": r'D:\pythonProject\test-task-selenuim-tenzor',
             'safebrowsing.enabled': True}
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.maximize_window()
    return browser
