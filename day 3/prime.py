# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:55:29 2019

@author: lenovo
"""
number = 1

while (number <= 10):
    diviser = 2
    
    while (diviser <= number):
     
        if (number % diviser == 0 and number != 2):
            break
        else:
            print (number)
            break
        diviser = diviser + 1
    number = number + 1
    
    
        
        