# This is the master stats script that opens and closes the others in their proper order
# Running the statistics script: 'dll_metastats.py, grabs and organizes 969 data, creates the necxessary workbook to pull these codes and Call#s together'
# # Statistics for Cataloging/Metadata Department (run monthly)
# Uses data from an OLE Report (item records and bib data)
# Figure out how to remove interm.csv documents and all other documents produced through the process
# jesse a lambertson lambertson@uchicago.edu

import sys, os

exec(open('call_counts.py').read())
exec(open('item_stats.py').read())
exec(open('969_stats.py').read())
exec(open('Stats_wb.py').read())

print('Workbook for the month created')

exec(open('osRemove.py').read()) # this might work
