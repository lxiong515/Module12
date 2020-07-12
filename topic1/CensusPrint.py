"""
Program: CensusPrint.py
Author:  Luke Xiong
Date: 7/12/2020

This file will read/edit and print data from CSV.
"""
import csv
from topic1.Class import NewClass

def AddTotalPop():
    #this method will add the total population in the CSV
    pop_sum=0
    for key in rank:
        pop_sum += int(rank[key].population.replace(',',''))
    print(pop_sum)

with open('Census.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    rank={}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        rank[str(row[0])] = NewClass(row[1],row[2], row[3], row[4], row[4], row[5], row[6])

lines = list()
members=input('Enter item to be deleted:')
with open('Census.csv', 'r') as readFile:
    reader=csv.reader(readFile)
    for now in reader:
        lines.append(row)
        for field in row:
            if field == members:
                lines.remove(row)
with open('mycsv.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

    #print(rank)
    #now access key in dictionary/print the population of Dallas
    print('Population of Dallas County: '+ (rank['1'].population))
    #now sum up population across all objects:

AddTotalPop()
