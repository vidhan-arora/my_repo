# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:38:33 2019

@author: lenovo
"""

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]    
min_order=100
new_order=list(map(lambda x : (x[0],x[2]*x[3]),orders))
new_list1=list(map((lambda x : (x[0],x[1]+10) if x[1] < 100 else x) ,new_order ))
print(new_list1) 