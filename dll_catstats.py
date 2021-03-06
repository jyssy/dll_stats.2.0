# This is the master stats script that opens and closes the others in their proper order
# Running the statistics script: 'dll_metastats.py, grabs and organizes, physical item stats, original and copy stats (print and electronic), 969 data, ordered call#s, and creates the necessary workbook to pull these codes and Call#s together'
# Statistics for Cataloging/Metadata Department (run monthly)
# Uses data from an OLE SQL Report (item records and bib data)
# Jesse A Lambertson jessel@phantomlandscapes.com



exec(open('call_counts.py').read())
exec(open('item_stats.py').read())
exec(open('969_stats.py').read())
exec(open('print.py').read())
exec(open('electronic.py').read())
exec(open('wlaw.py').read())
exec(open('stats_wb.py').read())
print('Workbook for the month created')
exec(open('osRemove.py').read())
