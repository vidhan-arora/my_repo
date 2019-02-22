# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 17:32:56 2019

@author: lenovo
"""

def add(list1):
    list3=[]
    
    sum1=0
    for i in list1:
        i=int(i)
        sum1=sum1+(i)
        list3.append(i)
    return sum1
def multiply(list4):
    list5=[]
    sum2=1

    for i in list4:
        i=int(i)
        sum2=sum2*(i)
        list5.append(i)
    return sum2
list2=input("enter the list").split(",")
def largest(list5):
    for i in range(0,len(list5)):
        c=0
        for j in range(0,len(list5)):
            if(list5[i]>list5[j]):
                c=c+1
            if c==len(list5)-1:
                return list5[i]
print(largest(list2))
def smallest(list5):
    for i in range(0,len(list5)):
        c=0
        for j in range(0,len(list5)):
            if(list5[i]<list5[j]):
                c=c+1
            if c==len(list5)-1:
                return list5[i]

list2=input("enter the list").split(",")
def sorting(list8):
    for i in range(0,len(list8)):
        i=int(i)
    list8.sort()
    return list8
print(sorting(list2))
def Print():
    
    
    print(add(list2))
    print(multiply(list2))
    
    print(smallest(list2))
    print(sorting(list2))
     
     
     
     
     
     
     
       
            
        
    
    
        


