# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 18:24:23 2019

@author: lenovo
"""
from functools import reduce
orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
         [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
new_order=list(map(lambda x: [x[0]]+list(map(lambda y:y[1]*y[2],x[1:])),orders))
new_order1 = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], new_order))
print(new_order1)