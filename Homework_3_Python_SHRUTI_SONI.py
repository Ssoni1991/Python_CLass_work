# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 11:49:07 2017

@author: Shruti

#Create a new file with the header row and the row for Roosevelt
#University and print the row number the data was on
 
"""

import csv

with open('D:\Fall_2017\python\university.csv', 'w') as csvfile:
    fieldnames = ['Student', 'UniversityName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Student': 'Shruti', 'UniversityName': 'Roosevelt University'})
    writer.writerow({'Student': 'Sanket', 'UniversityName': 'Depaul University'})
    writer.writerow({'Student': 'Hardik', 'UniversityName': 'Roosevelt University'})
    writer.writerow({'Student': 'Jalpa', 'UniversityName': 'Depaul University'})

string = 'Roosevelt University'

with open("D:\Fall_2017\python\university.csv") as myFile:
    for num, line in enumerate(myFile, 1):
        if string in line:
            print 'found at line:', num