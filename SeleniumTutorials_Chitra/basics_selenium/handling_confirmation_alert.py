'''
Created on 23 May 2025

@author: Chitra
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


'''3. Confirmation Alert'''

''' Clicking on confirmation alert button'''
confirmation_alert_btn = driver.find_element(By.ID, 'confirmBtn')
confirmation_alert_btn.click()

''' Switching to confirmation alert'''
confirmation_alert = driver.switch_to.alert

''' Printing the text on the confirmation alert'''
confirmation_alert_text = confirmation_alert.text
print(confirmation_alert_text)

time.sleep(3)

''' Accepting the confirmation alert/ `clicking 'OK' '''
confirmation_alert.accept()

time.sleep(3)

''' Clicking 'Cancel'''
confirmation_alert.dismiss()




