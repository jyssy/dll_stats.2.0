import csv, os
import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook

wb = Workbook()
ws = wb.active 

items = pd.read_csv('stats_out.csv', header=None) # the actual item-count statistics for each cataloger
callNos = pd.read_csv('CallNo_Count.csv', header=None) # to list the accumulation of physical materials in call# ranges
eBibedits = pd.read_csv('969_data.csv', header=None) # to count edits made to bibs for electronic, etc, not counted by item edits

ws1 = wb.create_sheet('Item Stats', 0)
ws2 = wb.create_sheet('CallNos', 0)
ws3 = wb.create_sheet('969 Stats', 0)

year = input('What year is it? ')
month = input('What month is it? ')

wb.save(year + '_' + month + '.DLL_CatalogingStats.xlsx')








