'''
Created on 23 May 2025

@author: Chitra
'''

'''

** For alert button, we cannot inspect on the 'OK' button, as it was written in javascript.**

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''3. Simple Alert'''

''' Clicking on simple alert button'''
simple_alert_btn = driver.find_element(By.ID, 'alertBtn')
simple_alert_btn.click()

''' Switching to simple alert'''
simple_alert = driver.switch_to.alert

''' Printing the text on the simple alert'''
simple_alert_text = simple_alert.text
print(simple_alert_text)

time.sleep(3)

''' Accepting the simple alert/ `clicking 'OK' '''
simple_alert.accept()


