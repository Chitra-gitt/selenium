'''
Created on 19 May 2025

@author: Chitra
'''


''' 1. Launching the chrome browser'''

from selenium import webdriver
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
#driver.get('https://selenium.dev/')
#driver =Chrome()


''' 2. Navigating to particular site'''

driver.get('https://testautomationpractice.blogspot.com/')


'''3. Upload a single file'''

single_file_input = driver.find_element(By.ID, 'singleFileInput')
single_file_input.send_keys('/Users/chitra/Downloads/sample test.rtf')

single_upload_btn = driver.find_element(By.XPATH, '//*[@id="singleFileForm"]/button')
single_upload_btn.click()


'''4. Upload a multiple file'''

multiple_files_input = driver.find_element(By.ID, 'multipleFilesInput')
multiple_files_input.send_keys('/Users/chitra/Downloads/sample test 1.rtf')
multiple_files_input.send_keys('/Users/chitra/Downloads/sample test 2.rtf')

multiple_upload_btn = driver.find_element(By.XPATH, '//*[@id="multipleFilesForm"]/button')
multiple_upload_btn.click()


