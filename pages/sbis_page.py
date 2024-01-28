from pages.base_page import BasePage
from selenium.webdriver.common.by import By


contact_btn_selector = (By.XPATH, "//*[@href='/contacts']")


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://sbis.ru')

    def contact_button(self):
        return self.find_element(contact_btn_selector)

    def click_contact_btn(self):
        self.contact_button().click()