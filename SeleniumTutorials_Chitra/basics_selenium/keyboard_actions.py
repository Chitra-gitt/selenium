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


'''4. Copy text from field1 (cmd+ a) and (cmd+ c)'''

field1_txt_bx = driver.find_element(By.XPATH, '//*[@id="field1"]')
actions.key_down(Keys.COMMAND, field1_txt_bx).send_keys('a').key_up(Keys.COMMAND).perform()

actions.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()


'''5. Pasting the text in field2 (cmd+v)'''

field2_txt_bx = driver.find_element(By.XPATH, '//*[@id="field2"]')
actions.key_down(Keys.COMMAND, field2_txt_bx).send_keys('v').key_up(Keys.COMMAND).perform()


