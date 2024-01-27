class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, args):
        return self.browser.find_element(*args)

    def switch_window(self, num):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[num])

