"""
Не могу переключаться на СБИС Плагин в сайдбаре и кликать по ссылке загрузки на странице загрузки через методы класса.
Постоянно теряю аргумент num
Буду признателен, если поможете разобраться)


from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sidebar_selector = (By.CLASS_NAME, 'controls-TabButton')
web_installer_selector = (By.XPATH, "//*[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")


class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Находим через класс родитель элемент сайдбара на странице. Вернется список, так как такой же айди имеет множество элементов
    def sidebar(self):
        return self.find_elements(sidebar_selector)

    # Кликаем на нужную нам плашку СБИС Плагин
    def select_sbis_plugin_on_sidebar(self, num):
        self.browser.find_elements(self.sidebar[num]).click()

    # Находим через класс родитель кнопки скачивания плагина
    def web_installer(self):
        return self.find_element(web_installer_selector)

    #Жмем на кнопку скачивания плагина
    def click_web_installer(self):
        self.web_installer.click()

"""
