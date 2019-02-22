# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:37:34 2019

@author: lenovo
"""
def leap_func(year):
    if(year%4==0):
        return True
    if(year%100==0):
        return False
    if(year%400==0):
        return True
    else: 
        return False
print(leap_func(2011))
print(leap_func(2016))