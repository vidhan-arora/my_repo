# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:32:39 2019

@author: lenovo
"""

age=int(input("enter the age"))
if(age==0 or age==1):
    print("infant")
elif(age>1 and age<=18):
    print("child")
    if(age>18 and age<=60):
        print("adult")
else:
    print("senior citizen")