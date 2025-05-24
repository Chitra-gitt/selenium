'''
Created on 24 May 2025

@author: Chitra
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v133.page import FrameScheduledNavigation
#import time

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://demo.automationtesting.in/Frames.html')

''' 3. Click on iframe within a iframe'''
iframe_with_in_an_iframe = driver.find_element(By.PARTIAL_LINK_TEXT, 'Iframe with in an Iframe')
iframe_with_in_an_iframe.click()

''' 4. Switch to outer frame(nested iframe)''' 
outer_frame = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer_frame)


''' 5. Switch to inner frame(iframe demo)'''
inner_frame = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_frame)


'''4. Enter text in the Frames '''
input_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
input_txt_bx.send_keys("Welcome")






