class BasePage:
    def __init__(self, browser):
        self.browser = browser

    # Определяем базовосу классу метод поиска элемента через метод вебдрайвера, который будут использовать
    # наследованные классы
    def find_element(self, args):
        return self.browser.find_element(*args)

    # Определяем базовосу классу метод поиска элементОВ через метод вебдрайвера, который будут использовать
    # наследованные классы
    def find_elements(self, args):
        return self.browser.find_elements(*args)

    # Этот метод выполняет переключение на новое окно, открытое в браузере. Аргументом - элемент списка
    def switch_window(self, num):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[num])
