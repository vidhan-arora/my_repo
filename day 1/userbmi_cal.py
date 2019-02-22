# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:06:15 2019

@author: lenovo
"""


weight=int(input("enter weight of person"))
#weight of a person
height=float(input("enter height of a person"))
#height of a person
to_bmi=weight//height
bmi=to_bmi//height
#this is done for converting into bmi
print(bmi)