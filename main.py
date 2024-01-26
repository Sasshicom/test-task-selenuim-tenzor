from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://sbis.ru/contacts')
banner = browser.find_element(By.CLASS_NAME, "sbisru-Contacts__logo-tensor").click()
time.sleep(1)



block_human_power = browser.find_element(By.CLASS_NAME, 's-Grid-col--6')
if block_human_power is None:
    print('None')
else:
    print('Yes')
time.sleep(1)

tabs = browser.window_handles
print(tabs)
browser.switch_to.window(tabs[1])
more_button = browser.find_element(By.XPATH, "//*[@href='/about']")
if more_button is None:
    print('None')
else:
    print('Yes')

#todo изменить метод нажатия на кнопку, пока тут такой костылик из за областей видимости
browser.execute_script("arguments[0].click();", more_button)

photo_grid_container = browser.find_element(By.CLASS_NAME, 's-Grid-container')
if photo_grid_container is None:
    print('None')
else:
    print('Yes')

time.sleep(2)
photo1 = browser.find_elements(By.CLASS_NAME, "tensor_ru-About__block3-image")
if photo1 is None:
    print('None')
else:
    print('Yes')
    print(photo1)

obj_img_width = []
obj_img_height = []
for photo in photo1:
    w = photo.get_attribute("width")
    h = photo.get_attribute("height")
    obj_img_width.append(w)
    obj_img_height.append(h)

print(obj_img_width)
print(obj_img_height)
browser.quit()

