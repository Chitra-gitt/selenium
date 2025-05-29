'''
Created on 29 May 2025

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

'''3. Print value from each cell'''

cell_21 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
cell_21_text = cell_21.text
print(cell_21.text)


cell_22 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_text = cell_22.text
print(cell_22.text)

cell_23 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_text = cell_23.text
print(cell_23.text)


cell_24 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]')
cell_24_text = cell_24.text
print(cell_24.text)


'''try same code using looping statement'''

