from pages.base_page import BasePage
from selenium.webdriver.common.by import By


banner_selector = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
region_span_selector = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
kamchatka_region_selector = (By.XPATH, "//*[@title='Камчатский край']")


class ContactPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_banner(self):
        return self.find_element(banner_selector)

    def click_banner(self):
        self.find_banner().click()

    def get_region(self):
        return self.find_element(region_span_selector).get_attribute("textContent")

    def click_region_span(self):
        self.find_element(region_span_selector).click()

    def select_new_region(self):
        self.find_element(kamchatka_region_selector).click()

    def partner_list(self):
        return self.browser.find_element(By.CLASS_NAME, 'sbisru-Contacts-List__name').get_attribute("title")
