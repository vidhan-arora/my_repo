# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:43:37 2019

@author: lenovo

"""
import random
winning_no=random.randint(1,10)



def vidhan():
    number=int(input("enter the number: "))
    if number==winning_no:
            print("you win ")
     break
            
    else:
            if number < winning_no:
                print("too low")
            else:
                print("too high")
vidhan()
for i in range(6,0,-1):
    print("you have  chance left",i)
    #choise=input("u want to play: ")
   # if choise== "yes":
    vidhan() 
    #else:
        #






