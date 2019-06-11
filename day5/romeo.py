# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:21:33 2019

@author: lenovo
"""
from  collections import Counter
with open('romeo.txt','rt')as file:
    aa=file.read().split(" ")
    
    frequency=Counter(aa)
    print(frequency)
    
    
list=[]
count=dict()
with open('romeo.txt','r')as file:
   for line in file:
        words=line.split(" ")
        list.append(words)
        for word in words:
            if word not in count:
                count[word]=1
            else:
                count[word]+=1
print(list)
print(count)