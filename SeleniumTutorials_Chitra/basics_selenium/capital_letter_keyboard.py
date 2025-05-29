'''
Created on 26 May 2025

@author: Chitra
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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

'''4. Capital letter - Name'''
name_txt_bx = driver.find_element(By.ID, 'name')
#name_txt_bx.send_keys("chitra")
actions.key_down(Keys.SHIFT,name_txt_bx).send_keys("chitra").key_up(Keys.SHIFT).perform()




