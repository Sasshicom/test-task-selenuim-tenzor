from pages.base_page import BasePage
from selenium.webdriver.common.by import By

more_btn_selector = (By.XPATH, "//*[@href='/about']")


class TenzorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @property
    def more_btn(self):
        return self.find_element(more_btn_selector)
