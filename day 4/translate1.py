# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:03:52 2019

@author: lenovo
"""

list3=input("enter the list").split(",")
def translate(a):
    list1=["a","e","i","o","u"]
    list2=[]
    for i in a:
        i=str(i)
        if i  not in list1:
            x=(i+"o"+i)
            list2.append(x)
        else:
            list2.append(i)
            for i in list2:
                print((i),end="")
print(translate(list3))
       