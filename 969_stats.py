import csv, sys
import operator

file_name = 'law969.csv' # make sure to pick a proper name for the 969 outout to be names for the script
f = open(file_name, encoding='utf-8')
csv_file = csv.reader(f)
next(csv_file)
second_column = [] # empty list to store eighth column values
for line in csv_file:
    second_column.append(line[1])

# removes empty lines, puts in required header file, strips out old header file
dataList=[s for s in second_column if s.strip()]
dataList.insert(0, 'iniCOD')
#dataList.remove('Item note')

# make the list object into a set object
dataSet=set(dataList)

team = dict(jal='Jesse Lambertson ', psm='Pat Sayre-McCoy ', mcd='Melanie Dial ', den='Daryl Nelson ', jrs='Julie Stauffer ', naa='Nissy ', dmd='Dora Davis ', ini='Initial_header ')
codes = dict(PMO=' Print Monograph Original ', PML=' Print Monograph LC copy ', PMC=' Print Monograph OCLC copy ', COD=' Code_header ',
                 PMR=' Print Monograph OCLC Revised ', PMB=' Print Monograph Rare Book cataloging ', PPC=' Print PCC Original ',
                 PCU=' Print PCC Upgrade ', PSO=' Print Serial Original ',
                 PSL=' Print Serial LC copy ', PSC=' Print Serial OCLC copy ', PSR=' Print Serial OCLC Revised ',
                 MWL=' Monograph WLAW ',MWR='Monograph WLAW Removed', WMO=' Web monograph Original ', WML=' Web Monograph LC Copy ',
                 WMC=' Web monograph OCLC copy ', WMR=' Revised web monograph ', WSO=' Web Serial Original ',
                 WSL=' Web Serial LC copy ', WSC=' Web Serial OCLC ', WSR=' Web Serial Revised ',
                 IOR=' Integrating Original Resource ', ICR=' Integrating OCLC Resource ', ILR=' Integrating LC Resource ', NNA=' New NACO Contribution ',
                 RNA=' Print Serial Enrich ', NSA=' New Series contribution ', RSA=' Revised Series contribution ',
                 RMB=' Revised Monograph Bibliographic ', RSB=' Revised Serial Bibliographic ', RIB=' Revised Integrating Bibliographic ', RWB=' Revised Web Bibliographic ',
                 DVO=' DVD Original ', DVC=' DVD OCLC copy ', DVL=' DVD LC Copy ',
                 ADD=' Added volume (added copy) ')

# Loop through the set.
# Count number of occurrences of each set element in the list
# Includes PCC BibCO (lambertson). NACO is, by necessity, collected separately.

with open('interim2.csv', 'w', newline='') as unsorted:
    # writer = csv.writer(stats_output, delimiter=':')
    writer = csv.writer(unsorted, delimiter=':')

    for stat in dataSet:

            name_stat = team[stat[:3]]
            code_stat = codes[stat[-3:]]
            statCount =dataList.count(stat)

#        '''Using 'write' in the csv module to output the necessary
#            info. '''

            if stat != 'iniCOD':

                writer.writerow([name_stat, code_stat, str(statCount)])

            else:

                print('all good for 969 info')

            # print(name + ': ' + code + ': ' + str(statCount))

# sort the data and save it to a new csv
data = csv.reader(open('interim2.csv'), delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort
      # now write the sort result into new CSV file

with open("969_data.csv", 'w', newline='') as final:
    fileWriter = csv.writer(final, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)      

print('complete! and yay for 969 step!')