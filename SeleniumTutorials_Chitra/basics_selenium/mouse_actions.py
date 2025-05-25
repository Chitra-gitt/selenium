'''
Created on 25 May 2025

@author: Chitra

*** for all mouse click and keyboard actions, .perform() is used to call that action
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Creating an object from ActionChains class'''
actions = ActionChains(driver)

'''4. Scrolling'''
actions.scroll_by_amount(0,2000).perform()

'''5. Mouse Hover'''
point_me = driver.find_element(By.XPATH, '//*[@id="HTML3"]/div[1]/div/button')
actions.move_to_element(point_me).perform()

time.sleep(3)

'''6. Double Click''' 
copy_text = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
actions.double_click(copy_text).perform()

'''7. Drag and Drop'''
actions.scroll_by_amount(0,500).perform()
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
actions.drag_and_drop(source, target).perform()

'''8. Slider'''
slider_right_box = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')
actions.drag_and_drop_by_offset(slider_right_box,100,0).perform()

# time.sleep(2)
# slider_left_box = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
# actions.drag_and_drop_by_offset(slider_left_box,0,30).perform()

'''9. '''
driver.get('https://demo.guru99.com/test/simple_context_menu.html')


