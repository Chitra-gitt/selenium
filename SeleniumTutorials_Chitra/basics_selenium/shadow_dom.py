'''
Created on 2 Jun 2025

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

'''3. Enter text in the Shadow DOM'''

'''3.a. Locate shadow host'''
shadow_host = driver.find_element(By.ID, 'shadow_host')

'''3.b. Get shadow root present in the shadow host'''
my_shadow_root = shadow_host.shadow_root

'''3.c. Find the element inside shadow root'''
input_text = my_shadow_root.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')
input_text.send_keys("Chitra")



