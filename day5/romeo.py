# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:21:33 2019

@author: lenovo
"""
from  collections import Counter
with open('romeo.txt','rt')as file:
    aa=file.read().split(" ")
    
    frequency=Counter(aa)
    print(frequency)     