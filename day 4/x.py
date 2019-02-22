# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:20:18 2019

@author: lenovo
"""

def filter_odd_even(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
   
number=[1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(number))