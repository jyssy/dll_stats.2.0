import csv, os, operator
import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook

wb = Workbook()
# ws = wb.active
ws1 = wb.create_sheet('Item Stats', 0)
ws2 = wb.create_sheet('969 Stats', 1)
ws3 = wb.create_sheet('CallNos', 2)

items = pd.read_csv('stats_out.csv', header=None) # the actual item-count statistics for each cataloger
items = dataframe_to_rows(items)
for r_idx, row in enumerate(items, 0):
    for c_idx, value in enumerate(row, 0):
         ws1.cell(row=r_idx, column=c_idx, value=value)
eBibedits = pd.read_csv('969_out.csv', header=None) # to count edits made to bibs for electronic, etc, not counted by item edits
eBibedits = dataframe_to_rows(eBibedits)
for r_idx, row in enumerate(eBibedits, 0):
    for c_idx, value in enumerate(row, 0):
         ws2.cell(row=r_idx, column=c_idx, value=value)
callNos = pd.read_csv('CallNo_Count.csv', header=None) # to list the accumulation of physical materials in call# ranges
callNos.sort_values(by=[0], axis=0, ascending=True, index=False, inplace=True)
callNos = dataframe_to_rows(callNos)
for r_idx, row in enumerate(callNos, 0):
    for c_idx, value in enumerate(row, 0):
         ws3.cell(row=r_idx, column=c_idx, value=value)

syear = input('What year is it? ')
smonth = input('What month is it? ')

wb.save(syear + '_' + smonth + '.DLL.CatalogingStats.xlsx')
