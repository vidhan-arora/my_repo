# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:18:34 2019

@author: lenovo
""" 
list2=input(map(int("enter the list"))).split(",")
def vidhan(list3):
   
    sum1=0

    for i in range(0,len(list3)):
        if(list3[i]==13):
            pass
        elif(13==list3[i-1]):
            pass
      
        sum1=sum1+list3[i]
       

    return sum1
print(vidhan(list2))
    
            
            
            