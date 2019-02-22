# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 18:31:04 2019

@author: lenovo
"""
dict1={}
str1=input("enter the name and number: ")
letter=0
digit=0


for item in str1:
    if item.isalpha():
        letter = letter + 1
    if item.isdigit():
        digit = digit + 1
        

dict1['letters'] = letter
dict1['digits'] =digit

print (dict1)
        