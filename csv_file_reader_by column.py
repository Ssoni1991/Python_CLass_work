# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:30:03 2017

@author: Shruti
"""

import csv


file = 'D:/Fall_2017/python/using_RELAFFIL.file_programming/RELAFFIL.csv'


def read_funding_data(path): #creating function , Declaring the function 
     with open(path,'rU') as data: #readable file in unicode 
         reader =csv.DictReader(data) #reader has datatype DictReader
         for row in reader: #every row in the fileoperated 
             yield row #create new thread
             

RELAFFIL={} #variable creation
for row in read_funding_data(file):
    RELAFFIL[row['code']]=row['category'] #assigning the value to the index . assiging the two column
    #data structure Key=code Value=Category
    
print RELAFFIL
print "######################"

RELAFFIL={}
for row in read_funding_data(file):
    RELAFFIL[row['code']]=row['category']
print RELAFFIL

# take any csv file 
#read from top to bottom  row by row 
#of the churches with affilieted schools, are more of them Episcopal or Baptist?