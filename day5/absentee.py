# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:55:05 2019

@author: lenovo
"""


    
count=0
while count < 25:
    with open('vidhan.txt' ,'a')as f:
        f.write(input('enter')+'\n')
        count=count+1
        