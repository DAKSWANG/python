# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 00:57:33 2017

@author: DAKS
"""

import sys
import re
import numpy as np
import pandas as pd

#s = open('msr_train-utf3.txt', encoding = 'utf8').read()
#s = s.split('\r\n')

count = 3
students = np.array([[1,5],[2,4],[3,3],[4,2],[5,1]])

urinals = np.zeros([count,2])
print (urinals)

for i in range(len(students)):
    for j in range(count):
        if (urinals[j,1]>0):
            urinals[j,1] = urinals[j,1] - 1
            if (urinals[j,1] == 0):
                urinals[j] = [0, 0]
        
    pos = False
    for j in range(count):
        if ((urinals[j,0]==0) and (not pos)):
            urinals[j] = [i+1, students[i,1]]
            pos = True
            
    if (not pos):
        print ("  Not enough")
        
    print(urinals)



#print(students.sum(axis = 1))

#a = students - [0, 1]
#print(a)

#a = students - [0, 1]
#a = sum(students[0][:])
#print(a)


