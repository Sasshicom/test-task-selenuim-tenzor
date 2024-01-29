from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# Тут определены селекторы для разных элементов на странице
contact_btn_selector = (By.XPATH, "//*[@href='/contacts']")
download_sbis_btn_selector = (By.XPATH, "//*[@href='/download?tab=ereport&innerTab=ereport25']")


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Открываем главную страницу сайта СБИС методом get вебдрайвера
    def open(self):
        self.browser.get('https://sbis.ru')

    # Находим через класс родитель кнопку Контакты на странице СБИС
    def contact_button(self):
        return self.find_element(contact_btn_selector)

    # Кликаем на кнопку контакты
    def click_contact_btn(self):
        self.contact_button().click()

    # Находим через класс родитель кнопку Скачать СБИС на главной странце СБИС
    def download_sbis_btn(self):
        return self.find_element(download_sbis_btn_selector)

    # Кликаем на кнопку Скачать СБИС
    def click_download_sbis_btn(self):
        self.download_sbis_btn().click()
