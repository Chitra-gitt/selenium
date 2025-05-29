'''
Created on 21 May 2025

@author: Chitra
'''
from basics_selenium.first_program import current_page_title
''' 1. Launching the chrome browser'''

from selenium import webdriver
from selenium.webdriver.common.by import By
#import time

options= webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
#driver.get('https://selenium.dev/')
#driver =Chrome()
driver.implicitly_wait(10)  #implicit wait- 10sec, if every element is available, code will 
                                #execute without waiting for other element


''' 2. Navigating to particular site'''

driver.get('https://testautomationpractice.blogspot.com/')

''' 3. Wiki search'''

wiki_search_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
wiki_search_input.send_keys("Selenium")

wiki_search_btn = driver.find_element(By.XPATH, '//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input')
wiki_search_btn.click()

#time.sleep(5) #this is python code, so no need to use this in selenium

wiki_search_btn = driver.find_element(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a')
wiki_search_btn.click()


current_page_title = driver.title
print(current_page_title)

#driver.switch_to.new_window('tab') to switch the search to new tab/window, 
                                        #have to assign driver to new window


window_handles_list = driver.window_handles
#print(window_handles_list)

driver.switch_to.window(window_handles_list[1])

'''
new_page_title = driver.title
print(current_page_title)
'''
history_link = driver.find_element(By.XPATH, '//*[@id="toc-History"]/a/div/span[2]')
history_link.click()






