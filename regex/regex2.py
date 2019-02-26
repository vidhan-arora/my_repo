# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:21:40 2019

@author: lenovo
"""
import re

email=input("enter the email: ").split(",")
for i in email:
    if re.findall(r'[-_]?\w+@\w+\.\D{2,4}',i):
       print(i)
      
    else:
        print("email was not proper")
