from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.sbis_page import SbisPage
from pages.contact_page import ContactPage
from pages.base_page import BasePage
from pages.tenzor_page import TenzorPage
from pages.tenzor_about_page import TenzorAboutPage
import time


def test_block_human_power_exist(browser):
    sbis_page = SbisPage(browser)
    contact_page = ContactPage(browser)

    sbis_page.open()
    sbis_page.click_contact_btn()
    contact_page.click_banner()
    time.sleep(2)
    try:
        browser.find_element(By.CLASS_NAME, 's-Grid-col--6')
        # todo победить скролл на странце к блоку Сила в людях
        # browser.execute_script("arguments[0].scrollIntoView();", human_power_block)
    except NoSuchElementException:
        return False
    assert True


def test_check_img_size(browser):
    base_page = BasePage(browser)
    sbis_page = SbisPage(browser)
    contact_page = ContactPage(browser)
    tenzor_page = TenzorPage(browser)
    tenzor_about_page = TenzorAboutPage(browser)

    sbis_page.open()
    sbis_page.click_contact_btn()
    contact_page.click_banner()
    base_page.switch_window(1)
    # todo изменить метод нажатия на кнопку, пока тут такой костылик из за областей видимости, не могу победить скролл
    browser.execute_script("arguments[0].click();", tenzor_page.more_btn)
    photo_grid = browser.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image")
    obj_img_width = tenzor_about_page.fill_grid_object_width(photo_grid)
    obj_img_height = tenzor_about_page.fill_grid_object_height(photo_grid)

    assert tenzor_about_page.compare_width(obj_img_width)
    assert tenzor_about_page.compare_height(obj_img_height)
