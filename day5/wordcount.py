# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 18:00:10 2019

@author: lenovo

Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.           
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    """
filename=input(">")
with open('new.txt',"rt" ) as file: 
    print(len(file.read()))
    file.seek(0,0)
    a=(file.read())
    
    a=a.strip().split() 
    print(len(a))
    file.seek(0,0)
    print(len(file.readlines()))
    a=set(a)
    print(len(a))




   