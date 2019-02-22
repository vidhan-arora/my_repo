# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:48:01 2019

@author: lenovo
"""

str1=input("enter the string")
temp=""
dict1 = {}
for i in range(0,len(str1)):
    if str1[i] not in temp:
        dict1[str1 [i]] = str1.count(str1[i])
        #a=(f"{str1 [i]}:{str1.count(str1[i])}")
        #print(a)
        temp=temp+str1[i]

dict2 = {}

str1 = input("enter the string")

for char in str1:
    if char in dict2.keys():
        dict2[char] = dict2[char] + 1
    else:
        dict2[char] = 1
print(dict2)
        
        
        