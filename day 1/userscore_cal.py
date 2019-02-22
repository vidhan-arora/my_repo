# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:55:30 2019

@author: lenovo
"""

maximum_marks=int(input("enter the maximum marks"))
#maximum marks
a1=int(input("enter the assignment 1  marks"))
a2=int(input("enter the assignment 2  marks"))
a3=int(input("enter the assignment 3  marks"))
#assignment marks
e1=int(input("enter the exam 1 marks"))
e2=int(input("enter the exam 2  marks"))
#exam marks
weight_score=(a1+a2+a3)*0.1+(e1+e2)*0.35
#to calculate weight score
print(weight_score)