from pages.base_page import BasePage
from selenium.webdriver.common.by import By


banner_selector = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")


class ContactPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_banner(self):
        return self.find_element(banner_selector)

    def click_banner(self):
        self.find_banner().click()

    def compare_width(self, obj):
        return all(x == obj[0] for x in obj)

    def compare_height(self, obj):
        return all(x == obj[0] for x in obj)
