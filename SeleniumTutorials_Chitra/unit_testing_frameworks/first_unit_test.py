'''
Created on 7 Jun 2025

@author: Chitra
'''

import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By

class OrangeHRMLoginTest(unittest.TestCase):


    def test_navigation_to_login_page(self):
        
        ''' 1. Launching the chrome browser'''
        
        options= webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        
        ''' 2. Navigating to Orange HRM site'''

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        ''' 3. Validate navigation is successful'''
        
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login123"
        expected_url_portion = "auth/login"
        actual_url = driver.current_url
        
        #self.assertEqual(actual_url, expected_url, "Navigation to OrangeHRM navigation is failed")
        self.assertIn(expected_url_portion,actual_url,"Navigation to OrangeHRM navigation is failed")
        
        
    def test_orangehrm_login(self):
        
        ''' 1. Launching the chrome browser'''
        
        options= webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(10)
        
        ''' 2. Navigating to Orange HRM site'''

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        ''' 3. Enter username'''
                
        username_txtbox = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username_txtbox.send_keys("Admin")
        
        ''' 4. Enter password'''
                
        password_txtbox = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password_txtbox.send_keys("admin123")
              
        ''' 5. Enter login'''
        
        login_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_button.click()
        
        '''6. Enter Dashboard'''
        
        # expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        # expected_url_portion = "dashboard/index"
        # actual_url = driver.current_url
        # self.assertIn(expected_url, actual_url, "Login failed")
                
        '''6. Validate whether login is successful'''
        expected_url_member = "dashboard/index"
        actual_url = driver.current_url
        
        self.assertIn(expected_url_member, actual_url, "Login failed")
        
        
        