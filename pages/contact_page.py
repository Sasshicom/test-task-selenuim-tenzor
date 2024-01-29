from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# Тут определены селекторы для разных элементов на странице
banner_selector = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
region_span_selector = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
kamchatka_region_selector = (By.XPATH, "//*[@title='Камчатский край']")


class ContactPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Находим на странице контактов баннер ТЕНЗОР
    def find_banner(self):
        return self.find_element(banner_selector)

    # Кликаем на баннер ТЕНЗОР
    def click_banner(self):
        self.find_banner().click()

    # Находим на странице контактов span выбранного региона и возвращаем его атрибут title
    def get_region(self):
        return self.find_element(region_span_selector).get_attribute("textContent")

    # Кликаем на плашку с регионом
    def click_region_span(self):
        self.find_element(region_span_selector).click()

    # Находим в открывшемся окне с регоинами нужный для нас Камчатский Край
    def select_new_region(self):
        self.find_element(kamchatka_region_selector).click()

    # Находим в списке партнеров первого сертифицированного партнера и возвращаем его атрибут title
    def partner_list(self):
        return self.browser.find_element(By.CLASS_NAME, 'sbisru-Contacts-List__name').get_attribute("title")
