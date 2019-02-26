# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:36:18 2019

@author: lenovo
"""
import re
mail=input("enter the mail").split(",")
for i in mail:
    if re.findall(r'[_-]?\w+@\w+\D{2,4}',i):
        print("valid")
    else:
        print("invalid")
