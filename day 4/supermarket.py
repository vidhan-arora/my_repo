# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:59:15 2019

@author: lenovo
"""
from collections import OrderedDict

dict1 = OrderedDict()

while True:
    inp = input("enter the name and price: ")
    if inp == "":
        break
    item_list=inp.split(" ")
    price = int(item_list[-1])
    item=" ".join(item_list[:-1])
    dict1[item] = dict1.get(item,0) + price
print(dict1)
    
