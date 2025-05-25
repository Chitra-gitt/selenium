'''
Created on 25 May 2025

@author: Chitra

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
driver.get('https://demo.guru99.com/test/simple_context_menu.html')

'''3. Creating an object from ActionChains class'''
actions = ActionChains(driver)

'''4. Context click/ Right click''' 
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
right_click_me_btn = driver.find_element(By.XPATH,'//*[@id="authentication"]/span')
actions.context_click(right_click_me_btn).perform()


