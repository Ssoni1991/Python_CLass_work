# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:56:25 2017

@author: Shruti
"""


from operator import itemgetter
from string import punctuation

w = {}  #word array
Number = 3 #total number required to output

obj1 = (word.strip(punctuation).lower() #split punctuation marks from line 
    for line in open("D:\\Fall_2017\\python\\sample.txt") # loop through line 
       for word in line.split()) #split each word from line 
                                         
for word in obj1: #itterate through each word in words_generator
    w[word] = w.get(word, 0) + 1 # increment the count and assign in array

find_no_words = sorted(w.iteritems(), key=itemgetter(1), reverse=True)[:Number] 

for word, frequency in find_no_words:
    #print top_words 
    
    print "%s: %d" % (word, frequency)