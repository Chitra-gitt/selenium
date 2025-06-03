'''
Created on 31 May 2025

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

'''3. Print the books name'''
row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_count = len(row_list)

column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
column_count = len(column_list)

#expected_book = input("Enter book name:")

# for j in range(2, rows_count+1):
#     for i in range(1, column_count+1):
#         table_cell = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[{i}]')
#         table_cell_value = table_cell.text
#         print(table_cell_value)
#

'''4. Print the books price'''

name = input("enter book name:")
    
for j in range(2, rows_count+1):
    #for i in range(4, column_count+1):
        book_name = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[1]')
        actual_book_name = book_name.text
        #print(book_name)
        if actual_book_name == name:
            price = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[4]')
            price = price.text
            print("Price of ", book_name, "is", price)
            break
else:
    print("book not found")
    
    
    
    