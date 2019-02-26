# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:23:10 2019

@author: lenovoui
"""
import re
city=input("enter the name").split(",")
for i in city:
    if re.findall(r'\w{2,4}\s\w{3}\s\w+\-\w+\-?\w?\-?\w?',i):
        print(i)
    else:
        print("invalid")