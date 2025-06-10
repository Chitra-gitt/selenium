'''
Created on 8 Jun 2025

@author: Chitra
'''

import openpyxl

filepath = "/Users/chitra/Desktop/Testdata-DDT.xlsx" 
my_workbook = openpyxl.load_workbook(filepath)
my_active_sheet = my_workbook.active
total_rows = my_active_sheet.max_row
print(total_rows)


total_columns = my_active_sheet.max_column
print(total_columns)


'''
o/p- 

12
4

'''
