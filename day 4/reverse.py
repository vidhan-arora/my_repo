# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:44:26 2019

@author: lenovo
"""

s = input("enter the string:")
def reverse(s):
    str2=""
    for i in s:
        str2=i+str2
    return str2
print(s)
print(reverse(s))
    