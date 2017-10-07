# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 11:52:52 2017

@author: Shruti
"""

import gzip
with gzip.open("DATAFILE", "rU") as datafile:
    with open("NEW_EXCELFILE.csv", "w") as f1:
        for lineNo,line in enumerate(datafile):   
                f1.write(line)
                if lineNo==5:
                    break
datafile.close()
f1.close()
