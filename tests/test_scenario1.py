from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from pages.sbis_page import SbisPage
from pages.contact_page import ContactPage
from pages.base_page import BasePage


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
    base_page = BasePage(browser)
    sbis_page = SbisPage(browser)
    contact_page = ContactPage(browser)
    sbis_page.open()
    sbis_page.click_contact_btn()
    contact_page.click_banner()
    base_page.switch_window(1)
    more_button = browser.find_element(By.XPATH, "//*[@href='/about']")
    # todo изменить метод нажатия на кнопку, пока тут такой костылик из за областей видимости
    browser.execute_script("arguments[0].click();", more_button)
    browser.implicitly_wait(5)
    about_tab_url = browser.current_url
    assert about_tab_url == ("https://tensor.ru/about")
    photo_grid = browser.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image")
    obj_img_width = []
    obj_img_height = []
    for photo in photo_grid:
        w = photo.get_attribute("width")
        h = photo.get_attribute("height")
        obj_img_width.append(w)
        obj_img_height.append(h)

    assert contact_page.compare_width(obj_img_width)
    assert contact_page.compare_height(obj_img_height)
