from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TenzorAboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def compare_width(self, obj):
        return all(x == obj[0] for x in obj)

    def compare_height(self, obj):
        return all(x == obj[0] for x in obj)

    def fill_grid_object_width(self, photo_grid_obj):
        photo_grid = photo_grid_obj
        obj_img_width = []
        for photo in photo_grid:
            w = photo.get_attribute("width")
            obj_img_width.append(w)

        return obj_img_width

    def fill_grid_object_height(self, photo_grid_obj):
        photo_grid = photo_grid_obj
        obj_img_height = []
        for photo in photo_grid:
            h = photo.get_attribute("height")
            obj_img_height.append(h)

        return obj_img_height
