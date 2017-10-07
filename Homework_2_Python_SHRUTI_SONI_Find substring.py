# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:36:18 2017

@author: Shruti
"""

import csv

#fin = open('D:/Fall_2017/python/using_RELAFFIL.file_programming/RELAFFIL.csv')
#words = ["Episcopal","Baptist"]
#found = {}
#count=0

#f = open('D:/Fall_2017/python/using_RELAFFIL.file_programming/out.csv','w')
count_B=0
count_E=0

with open("D:/Fall_2017/python/using_RELAFFIL.file_programming/RELAFFIL.csv", "rb") as f:
    csvreader = csv.reader(f, delimiter=",")

    for row in csvreader:
        if "Baptist" in row[1]:
            count_B = count_B+1
            print "Baptist",count_B
            #f.write(count_B)
        elif "Episcopal" in row[1]:
            count_E = count_E+1
            print "Episcopal",count_E
            #f.write(count_E) 
        else:
           print ""
#f.close()          

#Output is : Baptist is 6 and Episcopal is 5  