# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 00:01:57 2019

@author: lenovo
"""

def day_in_month(month):
    if(month=="januaury"):
        return 31
    if(month=="febuaury"):
        return 28
    if(month=="march"):
        return 31
    if(month=="april"):
        return 30
    if(month=="may"):
        return 31
    if(month=="june"):
        return 31
    if(month=="july"):
        return 31
    if(month=="august"):
        return 31
    if(month=="september"):
        return 30
    if(month=="october"):
        return 31
    if(month=="november"):
        return 30
    if(month=="december"):       
        return 31
    else:
        return False
print(day_in_month("januaury"))
print(day_in_month("febuaury"))
print(day_in_month("march"))
print(day_in_month("april"))
print(day_in_month("may"))
print(day_in_month("june"))
print(day_in_month("july"))
print(day_in_month("august"))
print(day_in_month("september"))
print(day_in_month("october"))
print(day_in_month("november"))
print(day_in_month("december"))

