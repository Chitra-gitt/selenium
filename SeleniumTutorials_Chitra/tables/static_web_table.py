'''
Created on 29 May 2025

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

'''3. Print value from each cell'''

cell_21 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
cell_21_value = cell_21.text
print(cell_21_value)


cell_22 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_value = cell_22.text
print(cell_22_value)

cell_23 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_value= cell_23.text
print(cell_23_value)


cell_24 = driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]')
cell_24_value = cell_24.text
print(cell_24_value)


'''try same code using looping statement'''
#
# //*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[2]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[3]
# //*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[4]

'''4. Print value from each cell using loop'''

row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_count = len(row_list)

column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
column_count = len(column_list)

expected_book = input("Enter book name:")

for j in range(2, rows_count+1):
    for i in range(1, column_count+1):
        table_cell = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[{i}]')
        table_cell_value = table_cell.text
        print(table_cell_value)
    


'''
cell_22 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_value = cell_22.text
print(cell_22_value)

cell_23 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_value = cell_23.text
print(cell_23_value)

cell_24 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]')
cell_24_value = cell_24.text
print(cell_24_value)


cell_31 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]')
cell_31_value = cell_31.text
print(cell_31_value)


//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]

//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]
'''

