# (Trainer Hands On)

#string and number
"Hello " + 5

"Hello " + str(5)

"Hello " - str(5)


#Multiply string and number
"Hello " * 5


#Printing Output to the screen using single quote
print ( 'FORSK TECHNOLOGIES' )

#Printing Output to the screen using double quote
print ( "FORSK TECHNOLOGIES" )


#Triple quotes to maintain formatting of the text
long_str = """ this is a 
                multiple line string
                end of the string """
print ( long_str)


#Using Triple Quotes to print quotation marks in string
long_str = """ "FORSK TECHNOLOGIES" """
print (long_str )




"""
Escape Codes
\n    Inserts a newline in the text at this point.
\t    Inserts a tab in the text at this point.

\b    Inserts a backspace in the text at this point.

\"    Inserts a double quote character in the text at this point
\'    Inserts a single quote character in the text at this point
\\    Inserts a backslash character in the text at this point.    

\uDDDD character from the Unicode Character Set ( DDDD is four hex digits )

http://jrgraphix.net/r/Unicode/0900-097F
https://www.branah.com/unicode-converter

"""

long_str = "\"FORSK TECHNOLOGIES\""
print (long_str )


#Printing with Escape Codes
print ( "\nFORSK\nTECHNOLOGIES\n")
print ( "\nFORSK\tTECHNOLOGIES\n")
print ( "\"FORSK TECHNOLOGIES\"")
print ( "\'FORSK TECHNOLOGIES\'")
print ( "\\FORSK TECHNOLOGIES\\")


#Printing a normal character ( a )  using Unicode
print (u'\u0061')


#Printing a Special character ( & )  using Unicode
print (u'\u0026')


#Printing a Devanagari Script Character  ( क  )  using Unicode
print (u'\u0915')


#Printing a Devanagari Script Character  ( नमस्ते , दुनिया  )  using Unicode
print (u'\u0928\u092E\u0938\u094D\u0924\u0947')



"""

Code Challenge
  Name: 
    Name Printing in English
  Filename: 
    name_english.py
  Problem Statement:
    Print your First Name and Last Name in Quotation. 
    Both the first name and Last name should be on different lines 
  Hint: 
     Use the Escape Code for quotation and new line
     Use + operator for string concatenation
  Input:
     Take input from keyboard
  Output:
    "Sylvester"
    "Fernandes"

"""


"""

Code Challenge
  Name: 
    Temperature of City
  Filename: 
    city_temp.py
  Problem Statement:
    Print the temperature of your city in Degree Celsius for the day  
  Hint: 
     Use \u00b0 as the unicode for Degree 
  Input:
     Take input from keyboard
  Output:
    26° C

"""



"""
Code Challenge
  Name: 
    Unicode Printing
  Filename: 
    unicode_print.py
  Problem Statement:
    Print the below string as it is   
    UNIX® and Sun Microsystem™ are Copyright ©, 2019 Oracle
  Hint: 
    Use unicode \u00AE for Registered ® 
    Use unicode \u00A9 for Copyright © 
    Use unicode \u2122 for TradeMark ™ 
  Input:
    No input required
  Output:
    UNIX® and Sun Microsystem™ are Copyright ©, 2019 Oracle
"""


"""

Code Challenge
  Name: 
    Name Printing in Hindi
  Filename: 
    name_hindi.py
  Problem Statement:
    Print your First Name and Last Name in Devanagari Script ( Hindi ) 
    with a comma in between   
  Hint: 
    http://jrgraphix.net/r/Unicode/0900-097F
  Input:
    No input required
  Output:
        सिल्वेस्टर , फर्नांडीस

"""




"""
Code Challenge
  Name: 
    Name Printing Checkerboard pattern
  Filename: 
    checker.py
  Problem Statement:
    Print the checkerboard pattern using escape Codes and Unicode 
    with multiple print statements and the multiplication operator 
  Hint: 
    Eight characters sequence in a line and 
    the next line should start with a space
    try to use the * operator for printing
  Input:
    No input required
  Output:
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *

"""

"""
Code Challenge
  Name: 
    BMI Help Screen
  Filename: 
    bmi_help.py
  Problem Statement:
    Print the BMI Value Help Screen   
  Hint: 
     Use triple quotes syntax for formatted text
  Input:
    No input required
  Output:
    World Health Organisation's BMI VALUES ( 8 Levels )
      Severe Thinness: less than 16 
      Moderate Thinness: between 16 and 16.9 
      Mild Thinness: between 17 and 18.4 
      Normal: between 18.5 and 24.9 
      Overweight: between 25 and 29.9        
      Obese Class I: between 30 and 34.9 
      Obese Class II: between 35 and 39.9 
      Obese Class III: 40 or greater 
"""


# Modular Programming and Modules

"""
Modules are files containing Python statements and definitions, like function and class definitions.

Kinds of Modules

There are different kind of modules:

    1. Those written in Python
        They have the suffix: .py
    2. Dynamically linked C modules
        Suffixes are: .dll, .pyd, .so, .sl, ...
    3. C-Modules linked with the Interpreter:
       
        
import numpy
numpy.__file__
     
A package is basically a directory with Python files and a file with the name __init__.py.
Packages are a way of structuring Python’s module namespace by using "dotted module names". 
A.B stands for a submodule named B in a package named A. 


"""




# Importing Modules
 
import math
 
math.sqrt ( 16 )
math.log ( 16, 2 )  
math.cos ( 0 )

# Renaming a Namespace
#How to use package Aliasing in python  
import math as MT
 
MT.sqrt ( 16 )
MT.log ( 16, 2 )  
MT.cos ( 0 )

# Importing Names from a Module Directly
#How to use specific functions from packages or modules in python 
from math import sqrt
sqrt ( 16 )


#How to use specific functions from packages or modules
#and also aliasing
from math import sqrt as square 
square ( 16 )



#How to use generate random numbers in python 
import random 
r1 = random.randint(0,10)
print (r1)



#How to clear the screen or console before printing
import os

# this only works when you run the program from terminal or cmd 
os.system("clear") # for mac or linux
os.system("cls")   # for windows 

"""
import math
math.__file__

import random
random.__file__
   
import os
os.__file__
"""

# Explain the String Slicing Concept Image

#Slicing of strings

newstr = "Monty Python"

#START
newstr [ 0 ]
newstr [ -1 ]
 
#START and END
newstr [ 6:10 ]
newstr [ -12:-7 ]
  
newstr [ : 5 ]
newstr [ 0 : ]
newstr [ : ]
   
#START END and STEPS
#skip items while slicing
newstr [ ::1 ]
newstr [ ::2 ]
   
#move backwards while slicing
newstr [ ::-1 ]
 
newstr [ 2 : 8 : -1]
 
newstr [ 8 : 2 : -1]




# Hands On 1
string = "Rajasthan"
#Print characters at the even index number 

# Hands On 2
string = "Rajasthan"
#Print the given string in reverse 

# Hands On 3
string = "Forsk Technologies"
#Print Forsk using slicing ( forward indexing Left to Right  )  

# Hands On 4
string = "Forsk Technologies"
#Print Technologies using slicing ( forward indexing Left to Right )  

# Hands On 5
string = "Forsk Technologies"
#Print Forsk using slicing ( Reverse indexing Right to Left  )  


# Hands On 6
string = "Forsk Technologies"
#Print Technologies using slicing ( forward indexing Right to Left )  


# Hands On 7
string = "Forsk Technologies"
#Print ksroF using slicing ( forward indexing Left to Right  )  

# Hands On 8
string = "Forsk Technologies"
#Print siesgolonhceT using slicing ( forward indexing Left to Right )  

# Hands On 9
string = "Forsk Technologies"
#Print Technologies Forsk using slicing ( forward indexing Left to Right  )  

# Hands On 10
string = "Forsk Technologies"
#Print Technologies Forsk using slicing ( Reverse indexing Right to Left )  



#Strings in python are Immutable 
newstr [ 0 ] = "m"
#or 
del newstr [ 0 ]
  
newstr [ 0 ] = "monty Python"
# Explain this with the object reference visual


"""
Global Inbuilt function ( len and del )
len ( newstr )
del ( newstr )
print ( newstr )
"""


# String functions 
# ( lower, upper, find, replace, strip, lstrip, rstrip, split, join) 
# creates a new copy of the string 

newstr = "    Monty Python    "
newstr.lower()
newstr.upper()
   
newstr.find('r')
newstr.find('P')
newstr.replace(' ','\n')
 
newstr.lstrip()
newstr.rstrip()
newstr.strip()
  
newstr.split()
newstr.index('M')

" ".join( string )



#to list all the functions for an object  
dir ( str )

#to check the syntax for a specific function of the object 
help ( str.strip )

# list of the Built-in functions, exceptions, and other objects
import builtins
dir(builtins)


#Formatting the string 
print("Hello {}, your balance is {}.".format("Ram", 23067.2346))
print("Hello {0}, your balance is {1}.".format("Ram", 23067.2346))
print("Hello {name}, your balance is {blc}.".format(name="Ram", blc=23067.2346))

name = input("Enter your Name >")
blc = input("Enter your Balance  > ")

print("Hello {}, your balance is {}.".format(name, blc))
print("Hello {name1}, your balance is {blc1}.".format(name1=name, blc1=blc))


"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""


"""
Code Challenge
  Name: 
    Area and Perimeter of Circle
  Filename: 
    circle.py
  Problem Statement:
    Take the radius of the circle from the keyboard as input from the user 
    Calculate the area and perimeter of it.
  Hint: 
    Pi * radius * radius is the area of circle
    2 * Pi * radius is the perimeter of circle 
    Use math module to get the value of Pi ( 3.14 ) 
  Input:
    Take the radius from the keyboard as input from the user.
"""


"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""


"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""


"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  them in reverse order with a space between them, find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""


"""
Code Challenge
  Name: 
    BMI in Hindi
  Filename: 
    bmi_cal_hindi.py
  Problem Statement:
    Convert the BMI program to use hindi titles while taking input and print weight, 
    height and BMI in Hindi script using formatted strings concept   
  Hint: 
     Create a copy of the old bmi_cal.py program and do modification
"""



"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format.py
  Problem Statement:
    This program prints out the following string in a specific format (see the output). 
  Hint: 
    The string should be printed using a single print statement only and the indexes shouldn't be counted manually.
  Input:

    This is a multi line string. This code challenge is to
    test your understanding about strings.
    You need to print some part of this string.
    From here print this text without manually counting the indexes.
  Output:
    From here print this text without manually counting the indexes.
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""


"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format3.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    W*e*l*c*o*m*e* *t*o* *P*i*n*k* *C*i*t*y* *J*a*i*p*u*r
"""



"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format4.py
  Problem Statement:
    This program accepts the user's first name and last name 
    Print them in reverse order with a space between them.
    Take Input from User 
    Your code should have only a single user input statement.  
  Hint:
    Try to serach for some function in the str using help() and dir()
  Input:
    Forsk Technologies
  Output:
    Technologies Forsk
"""


#Take the age as input from the user and print  
age = input("Enter your age>")
age = int(age)
print (age)

#More refined way
age = int(input("Enter your age >"))
print (age)


"""
Decision based on Comparison Operators ( Non Sequential )
==  Equal
!=  Not Equal
>   Greater Then
<   Less Then
>=  Greater Then and Equal To
<=  Less Then and Equal To 

  Perform the above comparison operators using some numbers to demonstrate True or False  
"""

"""
Control Flow using Conditional Statement ( if )
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
"""

#Take the age as input from the user and print  
age = int(input("Enter your age>"))

if ( age > 0 ):
  print ("Valid Age")


"""
Control Flow using Conditional Statement ( if and else )
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
else:
  STATEMENTS_WHEN_CONDITION_IS_FALSE
"""

#Take the age as input from the user and print  
age = int(input("Enter your age>"))
if ( age > 0 ):
  print ("Valid Age")
else:
  print ("Invalid Age")


"""
Logical Operators ( AND, OR, NOT )
and Logical AND ( True and True )
or Logical OR ( False or True )
! Logical NOT ( !True ) 
"""

# Hand On
# Take the age as input from the user and print whether he is an Adult or Child 
# If the age is between 0 and 18 he is a Child else he is Adult




"""
Chained Conditioning or switching Statement ( if elif and else )
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
elif OTHER_EXPRESSION:
    STATEMENTS_WHEN_OTHER_CONDITION_IS_TRUE
else:
    STATEMENTS_WHEN_CONDITION_IS_FALSE
"""


# Hand On
# Take the age as input from the user and print whether he is a infant, Child , 
# Adult,  Senior Citizen
# 0 - 1 is Infant
# > 1 and < than 18 is Child 
# > 18 and < 60 is Adult
# > 60 is Senior Citizen 



#False Conditions Values using the bool function 

bool(False)
bool(0)
bool(90)  
#Zero or any numeric value

bool(None)  
bool("") # Any empty sequence 
bool(()) # Any empty sequence 
bool([]) # Any empty sequence 
bool({}) # Any empty sequence 


#Perform the above comparison operators using some numbers to demonstrate True or False using the bool() function 

"""
Nested Conditional Statements
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
else:
    if x > y: 
        STATEMENTS_WHEN_OTHER_CONDITION_IS_TRUE
    else:
        STATEMENTS_WHEN_CONDITION_IS_FALSE
"""




"""
Looping technique using while 
while BOOLEAN_EXPRESSION:
    STATEMENTS
""" 

n = 0
while (n < 10):
  print (n)
  n = n + 1


n = 0 
while ( True ):
  print (n)
  n = n + 1
  if ( n == 10 ) :
    break # immediately exit the loop


# Hands On  1
# Print all the numbers from 1 to 10 using condition in while loop

# Hands On  2
#  Print all the numbers from 1 to 10 using while True loop

# Hands On 3
#  Print all the even numbers from 1 to 10 using condition in while loop

# Hands On 4
#  Print all the even numbers from 1 to 10 using while True loop

# Hands On 5
#  Print all the odd numbers from 1 to 10 using condition in while loop

# Hands On 6
#  Print all the odd numbers from 1 to 10 using while True loop

# Hands On 7
#  Print all the prime numbers from 1 to 10 using condition in while loop

# Hands On 8
#  Print all the prime numbers from 1 to 10 using while True loop



"""
Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 50(included). For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
    User Input not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

