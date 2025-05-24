'''
Created on 11 May 2025

@author: Chitra
'''

''' Launching the chrome browser'''

from selenium import webdriver

options= webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.get('https://selenium.dev/')
#driver = Chrome()

'''
from selenium import webdriver

from selenium.webdriver import Chrome, Safari

driver = Chrome()
driver = webdriver.Chrome()
#driver = Safari()
driver.get('https://selenium.dev/')
'''

''' Navigating to particular site'''

driver.get('https://testautomationpractice.blogspot.com/')

''' Validate navigation is successful'''

current_page_title= driver.title
print(current_page_title)

actual_page_title= "Automation Testing Practice"

if current_page_title == actual_page_title:
    print("Test is passed")
else:
    print("Test is failed")
    
    
    
