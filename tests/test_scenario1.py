from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from pages.sbis_page import SbisPage
from pages.contact_page import ContactPage


def test_block_human_power_exist(browser):
    browser.maximize_window()
    sbis_page = SbisPage(browser)
    contact_page = ContactPage(browser)
    sbis_page.open()
    sbis_page.click_contact_btn()
    time.sleep(2)
    contact_page.click_banner()
    try:
        browser.find_element(By.CLASS_NAME, 's-Grid-col--6')
    except NoSuchElementException:
        return False
    assert True


def test_check_img_size(browser):
    browser.maximize_window()
    browser.get('https://sbis.ru')
    browser.find_element(By.XPATH, "//*[@href='/contacts']").click()
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "sbisru-Contacts__logo-tensor").click()
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    more_button = browser.find_element(By.XPATH, "//*[@href='/about']")
    # todo изменить метод нажатия на кнопку, пока тут такой костылик из за областей видимости
    browser.execute_script("arguments[0].click();", more_button)
    time.sleep(2)
    photo1 = browser.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image")
    obj_img_width = []
    obj_img_height = []
    for photo in photo1:
        w = photo.get_attribute("width")
        h = photo.get_attribute("height")
        obj_img_width.append(w)
        obj_img_height.append(h)
    print(obj_img_width)
    print(obj_img_height)
# browser.quit()
