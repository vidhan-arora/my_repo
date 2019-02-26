# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:34:28 2019

@author: lenovo
"""
import re
number=(input("enter the no.")).split(",")
for i in number:
    if re.findall(r'[+\.-]?\w*\.\w+',i):
        print("True")
    else:
        print("False")
        
