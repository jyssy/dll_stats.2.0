import csv
import operator

#  change the name of the output from DBeaver with the name: '969_in.csv'
file_name = '969_in.csv'
f = open(file_name, encoding='utf-8')
csv_file = csv.reader(f)
next(csv_file)
second_column = [] #  empty list to store eighth column values
for line in csv_file:
    second_column.append(line[1])

# removes empty lines, puts in required header file, strips out old header file
dataList=[s for s in second_column if s.strip()]
dataList.insert(0, 'iniCOD')
#dataList.remove('Item note')

#  make the list object into a set object
dataSet=set(dataList)

team = dict(jal='Jesse Lambertson ', psm='Pat Sayre-McCoy ', mcd='Melanie Dial ', den='Daryl Nelson ', jrs='Julie Stauffer ', naa='Nissy ', dmd='Dora Davis ', ini='Initial_header ')
codes = dict(PMO=' Print Monograph Original ', PML=' Print Monograph LC Copy ', PMC=' Print Monograph OCLC Copy ', COD=' Code_header ',
                 PMR=' Print Monograph OCLC Copy Revised ', PMB=' Print Monograph Rare Book cataloging ', PPC=' Print PCC Original ',
                 PPU=' Print PCC Upgrade ', PSO=' Print Serial Original ',
                 PSL=' Print Serial LC Copy ', PSC=' Print Serial OCLC Copy ', PSR=' Print Serial OCLC Copy Revised ', PCO=' Print CONSER Original ', PCU=' Print CONSER Upgrade',
                 MWL=' Monograph WLAW ',MWR='Monograph WLAW Removed', WMO=' Web Monograph Original ', WML=' Web Monograph LC Copy ',
                 WMC=' Web Monograph OCLC Copy ', WMR=' Revised Web Monograph ', WSO=' Web Serial Original ',
                 WSL=' Web Serial LC Copy ', WSC=' Web Serial OCLC Copy', WSR=' Web Serial Revised ',
                 IOR=' Integrating Original Resource ', ICR=' Integrating OCLC Copy Resource ', ILR=' Integrating LC Resource ', NNA=' New NACO Contribution ',
                 RNA=' Print Serial Enrich ', NSA=' New Series contribution ', RSA=' Revised Series contribution ',
                 RMB=' Revised Monograph Bibliographic ', RSB=' Revised Serial Bibliographic ', RIB=' Revised Integrating Bibliographic ', RWB=' Revised Web Bibliographic ',
                 DVO=' DVD Original ', DVC=' DVD OCLC Copy ', DVL=' DVD LC Copy ',
                 ADM=' Added-Volume Monograph ', ADS=' Added-Volume Serial')

# Loop through the set.
# Count number of occurrences of each set element in the list
# Includes PCC BibCO (lambertson). NACO is, by necessity, collected separately.

with open('interim2.csv', 'w', newline='') as unsorted:
    #  writer = csv.writer(stats_output, delimiter=':')
    writer = csv.writer(unsorted, delimiter=':')

    for stat in dataSet:

            name_stat = team[stat[:3]]
            code_stat = codes[stat[-3:]]
            statCount =dataList.count(stat)

#        """Using 'write' in the csv module to output the necessary
#            info. """

            if stat != 'iniCOD':

                writer.writerow([name_stat, code_stat, str(statCount)])

            else:

                print('all good for 969 info')

            # print(name + ': ' + code + ': ' + str(statCount))

# sort the data and save it to a new csv
interim_file2 = open('interim2.csv', 'r')
data = csv.reader(interim_file2, delimiter = ',')
sortedlist = sorted(data, key=operator.itemgetter(0))    # 0 specifies according to first column we want to sort

with open('969_out.csv', 'w', newline='') as final:
    fileWriter = csv.writer(final, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)

interim_file2.close()
print('complete! and yay for 969 step!')
