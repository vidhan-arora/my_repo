# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:08:08 2019

@author: lenovo
"""

shopping_list=[]
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")
while True:
    new_item=input(">").split(",")
    if new_item=="done"or"DONE":
        break
    shopping_list.append(new_item)
    
    for item in shopping_list:
        print(item)
