from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sidebar_selector = (By.CLASS_NAME, 'controls-TabButton')


class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def sidebar(self):
        return self.find_elements(sidebar_selector)
