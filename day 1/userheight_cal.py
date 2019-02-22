# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:38:12 2019

@author: lenovo
"""

height=float(input("enter your height"))
one_foot = 0.3018
#one foot in meter
one_inch = 0.254
#one inch in meter
in_foot=height*one_foot
#5foot in meter
in_inch=height*one_inch
#11 inch in meter
height_1=in_foot+in_inch
print(height_1)
#for covert  in centimeter
in_cm=height_1*100
print(in_cm)