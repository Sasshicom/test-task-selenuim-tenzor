import time
from selenium.webdriver.common.by import By
from pages.sbis_page import SbisPage
#from pages.download_page import DownloadPage
import os


def test_download_plugin_and_check_size(browser):
    sbis_page = SbisPage(browser)
#    download_page = DownloadPage

    sbis_page.open()
    download_btn = sbis_page.download_sbis_btn()
    browser.execute_script("arguments[0].scrollIntoView();", download_btn)
    sbis_page.click_download_sbis_btn()
    time.sleep(1)
    sidebar = browser.find_elements(By.CLASS_NAME, 'controls-TabButton')
    time.sleep(1)
    sidebar[1].click()
    web_installer_btn = browser.find_element(By.XPATH,
                        "//*[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
    web_installer_btn.click()
    time.sleep(15)
    file_size = os.path.getsize(r'D:\pythonProject\test-task-selenuim-tenzor\sbisplugin-setup-web.exe')
    file_size_mb = float(str(file_size / 1048576)[0:4])
    assert file_size_mb == 7.02
