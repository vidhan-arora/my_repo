# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:27:28 2019

@author: lenovo
"""

with open('words.txt',mode='rt')as rf:
    with open('vidhan.txt',mode='wt')as wf:
        for line in rf:
           print( wf.write(line))
    