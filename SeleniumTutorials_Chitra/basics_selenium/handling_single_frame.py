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

'''3. Switch to iframe'''
driver.switch_to.frame('singleframe')


'''4. Enter in the Frames text box '''

frames_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
frames_txt_bx.send_keys("Hello")




