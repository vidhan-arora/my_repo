#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:44:05 2018

@author: ajoyfern
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 07:02:21 2017

@author: Forsk
"""

import re 
"""                         
search() versus match()
The match() function checks for a match only at the beginning of the string (by default) 
The search() function checks for a match anywhere in the string.
"""

"""
findAll()
findall(pattern, string, flags=0)
Finds all the possible matches in the entire sequence and 
returns them as a list of strings. Each returned string 
represents one match.
"""
#-------------------------------------
"""
There are methods like start() and end() to know the 
start and end position of matching pattern in the string.
"""

import re          
result = re.search(r'forsk', 'Forsk forsk Summer Bootcamp')     

print (result.start())
print (result.end())

#-------------------------------------

pattern=re.compile('mm')                                       

result=pattern.findall('Forsk Summer Bootcammp')
print (result)
     
result = re.findall(r'mm','Forsk Summer Bootcammp' )
print (result)
#------------------------------------
result=re.findall(r'\w*','ForskSummerBootcamp')         
print (result)

#to skip blanks
result=re.findall(r'\w+',' Forsk Summer Bootcamp')
print (result)

#-----------------------------------
result=re.findall(r'^\w+','Forsk Summer Bootcamp')
print (result)

#To find end
result=re.findall(r'\w+$','Forsk Summer Bootcamp ')
print (result)

result=re.findall(r'\w\w','Forsk Summer Bootcamp')
print (result)

#-----------------------------------
result=re.findall(r'@\w+\.\w+\.*\w*','abc.test@gmail.com, xyz@test.in,test.first@company.com nimish@gmail.co.in')
print( result)



#-----------------------------------
#find date format numbers
result=re.findall(r'\d{2}-\d{2}-\d{4}','Kunal 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#----------------------------------

li=['+91-7999999999', \
    '399999-999', \
    '99999x9999', '5999999999']


for val in li:
 if re.findall(r'\+?[0-9]{0,2}-?[5-9]{1}[0-9-]{9}',val):
     print ("yes")
 else:
     print ("no")

#------------------------------------------



import re

lst = []
reg = re.compile(r'^[+-]?\d*\.\d+$')

while True:
    inp = raw_input()
    if not inp:
        break
    res = re.match(reg,inp)
    if res:
        lst.append(True)
    else:
        lst.append(False)

print (lst)










