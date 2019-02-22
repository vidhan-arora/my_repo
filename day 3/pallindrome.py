# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:16:17 2019

@author: lenovo
"""

list1=[12,32,44,56,121]
for i in list1:
    i=str(i)
    if(i==i[::-1]):
        print("True")
    else:
        print("false")
    
    
    