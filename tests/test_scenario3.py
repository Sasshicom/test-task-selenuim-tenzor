import time
from selenium.webdriver.common.by import By
from pages.sbis_page import SbisPage
from pages.download_page import DownloadPage


def test_scenario3(browser):
    sbis_page = SbisPage(browser)
    download_page = DownloadPage
    sbis_page.open()
    time.sleep(2)
    download_btn = browser.find_element(By.XPATH, "//*[@href='/download?tab=ereport&innerTab=ereport25']")
    time.sleep(2)
    browser.execute_script("arguments[0].scrollIntoView();", download_btn)
    time.sleep(2)
    download_btn.click()
    time.sleep(3)
    plugin_switcher = browser.find_elements(By.CLASS_NAME, 'controls-TabButton')
    time.sleep(2)
    plugin_switcher[1].click()
    time.sleep(2)
    web_installer = browser.find_element(By.XPATH,
                                         "//*[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
    time.sleep(2)
    web_installer.click()
    time.sleep(3)
