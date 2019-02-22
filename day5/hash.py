# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:09:17 2019

@author: lenovo
"""
import hashlib
with open("romeo.txt","rt")as file:
    file_content= file.read()
    result=hashlib.sha1(file_content.encode())
    print(result.hexdigest())