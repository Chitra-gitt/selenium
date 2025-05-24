'''
Created on 15 May 2025

@author: Chitra

'''
''' Launching the chrome browser'''

from selenium import webdriver
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
#driver.get('https://selenium.dev/')
#driver =Chrome()


''' Navigating to particular site'''

driver.get('https://testautomationpractice.blogspot.com/')

'''1. Enter Name'''

name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("Chitra")
# name_txt_bx.click() # This is just an example syntax for clicking an web element

'''2. Enter Email'''

email_txt_bx = driver.find_element(By.ID, 'email')
email_txt_bx.send_keys("xyz@gmail.com")


'''3. Enter Phone Number'''

phone_txt_bx = driver.find_element(By.ID, 'phone')
phone_txt_bx.send_keys("9876543210")

'''4. Enter Address'''

textarea_txt_bx = driver.find_element(By.ID, 'textarea')
textarea_txt_bx.send_keys("Bangalore, Karnataka")

'''5.1. Enter Gender- Male'''

male_txt_bx = driver.find_element(By.ID, 'male')
male_txt_bx.click()


'''5.2 Enter Gender- Female'''

female_txt_bx = driver.find_element(By.ID, 'female')
female_txt_bx.click()

'''6. Enter Days'''

#Sunday

sunday_txt_bx = driver.find_element(By.ID, 'sunday')
sunday_txt_bx.click()

#Monday

monday_txt_bx = driver.find_element(By.ID, 'monday')
monday_txt_bx.click()

#Tuesday

tuesday_txt_bx = driver.find_element(By.ID, 'tuesday')
tuesday_txt_bx.click()

#Wednesday

wednesday_txt_bx = driver.find_element(By.ID, 'wednesday')
wednesday_txt_bx.click()

#Thursday

thursday_txt_bx = driver.find_element(By.ID, 'thursday')
thursday_txt_bx.click()

#Friday

friday_txt_bx = driver.find_element(By.ID, 'friday')
friday_txt_bx.click()

#Saturday

saturday_txt_bx = driver.find_element(By.ID, 'saturday')
saturday_txt_bx.click()

'''7. Enter Country'''

country_txt_bx = driver.find_element(By.ID, 'country')
country_txt_bx.send_keys("Country")

# '''8. Enter Colours'''
#
# colours_txt_bx = driver.find_element(By.ID, 'colours')
# colours_txt_bx.send_keys("Colours")
#
# '''9. Enter Sorted list'''
#
# animals_txt_bx = driver.find_element(By.ID, 'animals')
# animals_txt_bx.send_keys("Animals")

'''10. Enter Date'''

# Date Picker 1 (mm/dd/yyyy) 

datepicker_txt_bx = driver.find_element(By.ID, 'datepicker')
datepicker_txt_bx.send_keys("Datepicker")

# Date Picker 2 (dd/mm/yyyy)

# txtdate_txt_bx = driver.find_element(By.ID, 'txtdate')
# txtdate_txt_bx.send_keys("txtdate")

