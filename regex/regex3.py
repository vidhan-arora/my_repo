# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:18:42 2019

@author: lenovo
"""
import re
card_no=input("enter the no: ").split(",")
for i in card_no:
    if re.findall(r'^[456]+\d{3}-?\d{4}-?\d{4}-?\d{4}',i):
        print("valid")
    else:
        print("invalid")