# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:42:43 2019

@author: lenovo
import re
name=input("enter the name: ").split(",")
for i in name:
    if re.findall(r'j\w+\sneu$',i):
        print(name)
    else:
        print("invalid name")