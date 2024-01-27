import time
from pages.sbis_page import SbisPage
from pages.contact_page import ContactPage


def test_check_region(browser):
    sbis_page = SbisPage(browser)
    contact_page = ContactPage(browser)
    sbis_page.open()
    sbis_page.click_contact_btn()

    assert contact_page.get_region() == "Новосибирская обл."
    assert contact_page.partner_list() == "СБИС - Новосибирск"


def test_switch_region(browser):
    sbis_page = SbisPage(browser)
    contact_page = ContactPage(browser)
    sbis_page.open()
    sbis_page.click_contact_btn()
    contact_page.click_region_span()
    time.sleep(2)
    contact_page.select_new_region()
    time.sleep(2)
    about_tab_url = browser.current_url
    new_title = browser.title

    assert contact_page.get_region() == "Камчатский край"
    assert about_tab_url == ("https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients")
    assert contact_page.partner_list() == "СБИС - Камчатка"
    assert new_title == "СБИС Контакты — Камчатский край"
