# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 18:00:10 2019

@author: lenovo
"""

filename=input(">")
with open(filename,"rt" ) as file: 
    print(len(file.read()))
    file.seek(0,0)
    a=(file.read())
    
    a=a.strip().split() 
    print(len(a))
    file.seek(0,0)
    print(len(file.readlines()))
    a=set(a)
    print(len(a))




   