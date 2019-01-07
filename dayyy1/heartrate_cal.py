# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:13:47 2019

@author: lenovo
"""

age=21
#given age
maximum_heart_rate= 220-age
#for calculate maximum heart rate
lowerendof_target_heart_rate=70
#lower end target heart rate
higherendof_target_heart_rate=85
#higher end target heart rate
target_heart_rate=lowerendof_target_heart_rate+higherendof_target_heart_rate//100*100
#for calculating target heart rate
print(maximum_heart_rate)
print(target_heart_rate)