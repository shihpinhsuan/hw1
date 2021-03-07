# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '108061229.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

target_data = data[:]

Alist = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
output = []

for item in Alist:
    max = 0
    min = float('inf')
    for Adata in target_data:
        if (Adata['WDSD'] != '-99.000' and Adata['WDSD'] != '-999.000') :
            if (Adata['station_id'] == item) :
                if (float(Adata['WDSD']) > max) :
                    max = float(Adata['WDSD'])
                if (float(Adata['WDSD']) < min) :
                    min = float(Adata['WDSD'])
    if (min == float('inf')):
        output.append([item, 'None'])
    else :
        output.append([item, max - min])
    
print(sorted(output, key = lambda t : t[0]))

#=======================================


# Part. 4

#=======================================

# Print result

#print(target_data)

#========================================