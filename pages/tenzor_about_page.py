from pages.base_page import BasePage


class TenzorAboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Метод получает на вход объект photo_grid в виде photo_grid_obj, найденный в test_scenario1
    # Итерируясь по объекту мы пробегаемся по каждому элементу и вытаскивает атрибут width
    # После каждой итерации мы добавляем в массив obj_img_width значение атрибута width итерируемого элемента
    def fill_grid_object_width(self, photo_grid_obj):
        photo_grid = photo_grid_obj
        obj_img_width = []
        for photo in photo_grid:
            w = photo.get_attribute("width")
            obj_img_width.append(w)

        return obj_img_width

    # Метод получает на вход объект photo_grid в виде photo_grid_obj, найденный в test_scenario1
    # Итерируясь по объекту мы пробегаемся по каждому элементу и вытаскивает атрибут height
    # После каждой итерации мы добавляем в массив obj_img_height значение атрибута height итерируемого элемента
    def fill_grid_object_height(self, photo_grid_obj):
        photo_grid = photo_grid_obj
        obj_img_height = []
        for photo in photo_grid:
            h = photo.get_attribute("height")
            obj_img_height.append(h)

        return obj_img_height

    # Метод принимает на вход obj_img_width в виде obj. Используя метод all мы итерируемся по каждому элементу
    # И сравниваем каждый элемент с нулевым значением массива obj (тавтология).
    # Метод all вернет true, если каждый из obj[x] == obj[0]
    def compare_width(self, obj):
        return all(x == obj[0] for x in obj)

    # Метод принимает на вход obj_img_height в виде obj. Используя метод all мы итерируемся по каждому элементу
    # И сравниваем каждый элемент с нулевым значением массива obj (тавтология).
    # Метод all вернет true, если каждый из obj[x] == obj[0]
    def compare_height(self, obj):
        return all(x == obj[0] for x in obj)
