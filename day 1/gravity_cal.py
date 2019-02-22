# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:43:21 2019

@author: lenovo
"""

time=int(input("enter the time"))
#time in minute
acceleration=bool(input("enter the accleration"))
#user input the accleration 
position_of_the_object= (acceleration*time*time ) / 2
#to find the position
print(position_of_the_object)