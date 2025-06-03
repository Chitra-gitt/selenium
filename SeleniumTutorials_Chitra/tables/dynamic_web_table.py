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

'''3. Dynamic table'''

# //*[@id="rows"]/tr[3]/td[1]//following-sibling::td[contains(text(), 'MB') and not(contains(text(), '/s'))]

''' *** MEMORY ***'''

row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)
    
expected_name = input("Name:")
    
for j in range(2, rows_count+1):
        name_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]')
        actual_name = name_cell.text
        if expected_name == actual_name:
            memory_cell = driver.find_element(By.XPATH, f"//*[@id='rows']/tr[{j}]/td[contains(text(),'MB')and not(contains(text(), '/s'))]")
            memory = memory_cell.text
            print(memory)
            break
else:
    print("Memory not found")        
    
    
# //*[@id="rows"]/tr[1]/td[3]
# //*[@id="rows"]/tr[1]/td[3]
#//*[@id="rows"]/tr[1]/td[3]'
#//td[contains(text(),'MB')and not(contains(text(), '/s'))]


''' *** NETWORK ***'''
 
row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)
    
expected_name = input("Name:")
    
for j in range(2, rows_count+1):
        name_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]')
        actual_name = name_cell.text
        if expected_name == actual_name:
            network_cell = driver.find_element(By.XPATH, f"//*[@id='rows']/tr[{j}]/td[contains(text(),'Mbps')]")
            network = network_cell.text
            print(network)
            break
else:
    print("Network not found")       
        
        
'''        
o/p-  :)

Name:Chrome
66.9 MB
Name:Chrome
4.5 Mbps
        
    # //*[@id="rows"]/tr[{j}]/td
    
    # //*[@id="rows"]/tr[1]
    # //*[@id="rows"]/tr[1]/td[4]
   # //td[contains(text(), 'Mbps')]
   #
   # //*[@id="rows"]
   # //*[@id="rows"]/tr[1]
   # //*[@id="rows"]/tr[1]/td[4]
   #//*[@id="rows"]/tr[1]/td[1]
   '''
   
   
'''*** Disk ***'''

row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)
    
expected_name = input("Name:")
    
for j in range(2, rows_count+1):
        name_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]')
        actual_name = name_cell.text
        if expected_name == actual_name:
            disk_cell = driver.find_element(By.XPATH, f"//*[@id='rows']/tr[{j}]/td[contains(text(),'MB/s')]")
            disk = disk_cell.text
            print(disk)
            break
else:
    print("Disk not found")       

'''
   o/p- :)
  
  Name:Chrome
62.9 MB
Name:Chrome
2.2 Mbps
Name:Chrome
0.12 MB/s
''' 
    
'''*** CPU ***'''
    
row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)
    
expected_name = input("Name:")
    
for j in range(2, rows_count+1):
        name_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[{j}]/td[1]')
        actual_name = name_cell.text
        if expected_name == actual_name:
            cpu_cell = driver.find_element(By.XPATH, f"//*[@id='rows']/tr[{j}]/td[contains(text(),'%')]")
            cpu = cpu_cell.text
            print(cpu)
            break
else:
    print("CPU not found")       
    
'''
o/p- :)

Name:Chrome
67.2 MB
Name:Chrome
2.8 Mbps
Name:Chrome
0.37 MB/s
Name:Chrome
2.7%

'''    
    
    
    