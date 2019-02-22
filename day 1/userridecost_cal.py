# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:10:41 2019

@author: lenovo
"""

travel=int(input("enter the travelling hours"))
#travel in a day
costof_diesel=int(input("cost of diesel "))
#cost of diesel per liter
avg=int(input("enter the avg. of car"))
#avg.of fuel kmper liter
costof_driving=travel*costof_diesel/avg
#to calculating the cost of driving
print(costof_driving)