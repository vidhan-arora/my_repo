"""
Any & All in Python

Any and All are two built ins provided in python used for successive And/Or.

Any

Returns true if any of the items is True. 
It returns False if empty or all are false.
Any can be thought of as a sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.

"""


# Since all are false, false is returned 
print (any([False, False, False, False])) 
  
# Here the method will short-circuit at the 
# second item (True) and will return True. 
print (any([False, True, False, False])) 
  
# Here the method will short-circuit at the 
# first (True) and will return True. 
print (any([True, False, False, False])) 


"""

All

Returns true if all of the items are True (or if the iterable is empty). 
All can be thought of as a sequence of AND operations on the provided iterables. 
It also short circuit the execution i.e. stop the execution as soon as the result is known.

"""


# Here all the iterables are True so all 
# will return True and the same will be printed 
print (all([True, True, True, True])) 
  
# Here the method will short-circuit at the  
# first item (False) and will return False. 
print (all([False, True, True, False])) 
  
# This statement will return False, as no 
# True is found in the iterables 
print (all([False, False, False])) 



"""

Truth table

+-----------------------------------------+---------+---------+
|                                         |   any   |   all   |
+-----------------------------------------+---------+---------+
| All Truthy values                       |  True   |  True   |
+-----------------------------------------+---------+---------+
| All Falsy values                        |  False  |  False  |
+-----------------------------------------+---------+---------+
| One Truthy value (all others are Falsy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| One Falsy value (all others are Truthy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| Empty Iterable                          |  False  |  True   |
+-----------------------------------------+---------+---------+



"""

# Advanced Collection ( Counter, OrderedDict, NamedTuple, Deque ) 

# check the frequency of the words

words = ["one", "two", "one", "two", "three", "four", "one"]

freq = dict()

for word in words:
    if word in freq:
        freq[word] += 1     
    else: 
        freq[word] = 1              


for key in freq.keys(): 
    print (key, ":", freq[key])
 
for key,value in freq.items():
    print (key, ":", value)


# Using default dict
from collections import defaultdict

words = ["one", "two", "one", "two", "three", "four", "one"]

freq = defaultdict(int)

# We have removed the logic to check whether key is present or not
for word in words:
    freq[word] += 1                   
        
for key in freq.keys(): 
    print (key, ":", freq[key])
 
for key,value in freq.items():
    print (key, ":", value)



# Alternate solution using Counter class 
    
from collections import Counter

words = ["one", "two", "one", "two", "three", "four", "one"]
frequency = Counter(words)
print (frequency)

for key,value in dict(frequency).items():
    print (key,value)

 
    
# OrderedDict 
    
# An OrderedDict is a dictionary subclass that remembers the order that 
# keys were first inserted. 
  
# OrderedDict preserves the order in which the keys are inserted. 
# A regular dict doesn’t track the insertion order, and iterating it gives the 
# values in an arbitrary order.

"""    
print ('Regular Dictionary:' )
d = dict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print ( k, v )


import collections

print ('Ordered Dictionary:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print ( k, v )

    
"""

    
# namedtuple
# Writing clean python

"""
When to Use Namedtuples

Namedtuples can be an easy way to clean up your code and to make it more 
readable by enforcing a better structure for your data.

I find, for example, that going from ad-hoc data types like dictionaries 
with a fixed format to namedtuples helps me express my intentions more 
clearly. Often when I attempt this refactoring I magically come up with 
a better solution for the problem I’m facing.

"""
    
import collections
# regular tuple 
# 55 represents RED, 155 represents GREEN and 255 represents BLUE 
color = ( 55, 155, 255 ) 
print ( color[0] ) # This leads to non readable tuples 


#Solution is NAMEDTUPLE
Color = collections.namedtuple('myColor', ['red','green','blue'])

print (type(Color))

color = Color ( blue=255, green=155, red = 55 )

print (type(color))

print ( color[0] ) 

print ( color.red )


# Returning Multiple Values From a Function
"""
Functions return one thing. 
When we return multiple values, we’re actually creating a tuple and 
returning it (again, one value).

As the number of values to return grows, the code becomes harder to read. 
In particular I have the rule of thumb, that for more than 3 arguments, 
namedtuples should always be used instead.

"""

def fetch_data():
     return 42, 'jsmith', 'John', 'Smith'

# Or
     
from collections import namedtuple

UserRecord = namedtuple("UserRecord", ('user_id', 'username', 'first_name', 'last_name'))

def fetch_data2():
    return UserRecord(42, 'jsmith', 'John', 'Smith')
    
mydata = fetch_data2()

print (type(mydata))    
print (mydata.user_id)      # instead of mydata[0]
print (mydata.username)     # instead of mydata[1]
print (mydata.first_name)   # instead of mydata[2]
print (mydata.last_name)    # instead of mydata[3]



# Deque
     
# Deque is a Double Ended Queue where operations(Add/Remove) can be made on both ends
# of the queue.
    
# Real Life Examples
# A web browser's history.
# storing a software application's list of undo operations
# stocks you last visited, it will remove the stocks after some time 
# and will add the latest ones.
# Job scheduling in a multiprocessor environment.
    

import collections

d = collections.deque('abcdefg')
print ('Deque:', d)
print ('Length:', len(d))
print ('Left end:', d[0])
print ('Right end:', d[-1])

d.remove('c')
print ( d )




# List Comprehension  and Lambda, Filter, Map, Reduce and zip
 

# List Comprehension 

""""
List comprehensions are used for creating new list from another iterables.
As list comprehension returns list, they consists of brackets containing 
the expression which needs to be executed for each element along with the 
for loop to iterate over each element.

Basic syntax:

new_list = [expression for_loop_one_or_more_conditions]
"""

# Find squares of a number using for loop.
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n**2)
print(squares)  



# Finding squares using list comprehensions
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)  



a = [1,2,3]
print ([ x**2 for x in a ])
print ([ x + 1 for x in [x**2 for x in a ]])



# Find common numbers from two list using list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)


#List comprehensions can also be used to iterate over strings as shown below:
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [str.lower() for str in list_a]
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']


# Just like tuples list comprehensions can be used to produce list of list as shown below.
list_a = [1, 2, 3]
square_cube_list = [ [a**2, a**3] for a in list_a]
print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]



# Lambda

"""
Lambda is a way to create anonymous function i.e. functions without name 
Lambda function are mainly used with Filter, Map and Reduce 
Lambda operator or lambda function is used for creating small, 
one-time and anonymous function objects in Python.

Syntax:
lambda arguments: expression
This function can have any number of arguments but only one expression, 
which is evaluated and returned.

"""

 
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y; 

print(cube(5))


# Converting the function to lambda function  
g = lambda y: y*y*y 
print (type(g))
print(g(5))  


# Lambda with two arguments 
f  = lambda x,y : x + y
print(f(1,1))




# Explain the concept of filter map reduce using the example of getting multiple  
# Temperature every sec using an IoT device


# Filter 
"""
The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence "sequence", 
for which the function returns True.
""" 

def f(x) :
    return x%3 ==0 or x%5 ==0 

list(range(2,25 ))

list(filter ( f, range(2,25 ) ))

print( list(filter ( f, range(2,25 ) ) ))


# Filter with Lambda function 
foo = list(range(2,25 ))

print (list ( filter (lambda x:x%3==0 or x%5==0,foo) ) )



# Map 

"""
map() function returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :
Returns a list of the results after applying the given function to each item 
of a given iterable (list, tuple etc.) 
"""

# Return double of n 
def addition(n): 
  return n + n 

# We double all numbers using map() 
numbers = [1, 2, 3, 4] 
result = map(addition, numbers) 
print(list(result)) 


# Double all numbers using map and lambda 
numbers = [1, 2, 3, 4] 
result = map(lambda n: n + n, numbers) 
print(list(result)) 



# Multiple iterables to the map function

# Add two lists using map and lambda 
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 


result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 


# List of strings 

l = ['sat', 'bat', 'cat', 'mat'] 
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 




# Need to get multiple integer inputs in the same line

#Way 1:
s = input()
print (s)
print(type(s))
s = s.split(',')
print(s)
s = [int(i) for i in s]

#Way 2:
s = [int(i) for i in input().split(',')]


#Way 3:
a = map(int, input().split(','))



# Reduce

"""
The reduce() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list. 
This is a part of functools module
"""


from functools import reduce
def add(x,y):
    return x+y

reduce ( add, range(1,11))

# Reduce with Lambda function 
foo = [2,18,9,22,17,24,8,12,27]
print (reduce (lambda x,y : x + y,foo))


# zip

"""
In Python3, zip methods returns a zip object instead of a list. 
This zip object is an iterator. Iterators are lazily evaluated.
Lazy evaluation, or call-by-need is an evaluation strategy which 
delays the evaluation of an expression until its value is needed 
and which also avoids repeated evaluations
Iterators returns only element at a time. 
len function cannot be used with iterators. 
We can loop over the zip object or the iterator to get the actual list
"""


list_a = [1, 2, 3]
list_b = [4, 5, 6]

zipped = zip(list_a, list_b) # Output: Zip Object. <zip at 0x4c10a30>

print(list(zipped))

len(zipped) # TypeError: object of type 'zip' has no len()

zipped[0] # TypeError: 'zip' object is not subscriptable

list_c = list(zipped) #Output: [(1, 4), (2, 5), (3, 6)]

list_d = list(zipped) # Output []... Output is empty list becuase by the above statement zip got exhausted.


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, which returns a list with 2-tuples. 
    Each tuple consists of a the order number and the product of the price per items 
    and the quantity. 
    The product should be increased by 10€ if the value of the order is smaller 
    than 100,00 €.

  Hint: 
    Write a Python program using lambda and map.

"""

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
    
    Write a program which returns a list of two tuples with 
    (order number, total amount of order).
    
    [ 1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], ... ]
    
  Hint: 
    from functools import reduce
"""


# Modular Programming and Modules
# Designing and Writing Modules

#__main__  concept

# first_module.py

print ("First Module name: {}".format(__name__))


#python first_module.py 
#This will print __main__




#second_module.py

import first_module
print ("Second Module name: {}".format(__name__))

#python second_module.py 
"""
This will print the first module name as first_module
but the second module name will be __main__

__main__ is printed in which the python runs the file
But if a file is imported then the variable is set to that file name

Every time a file is imported the file is run 

from imp import reload
reload(first_module) to reload a module in memory  
"""

# Packages in Python

# Directory with a name simple_package

# The content of a.py:
def bar():
    print("Hello, function 'bar' from module 'a' calling")

# The content of b.py:
def foo():
    print("Hello, function 'foo' from module 'b' calling")

# empty file with the name __init__.py inside of simple_package directory. 


from simple_package import a, b
a.bar()
b.foo()
    

"""
args and kwargs concept

The special syntax, *args and **kwargs in function definitions is used to 
pass a variable number of arguments to a function. 

"""
def test_var_args(farg, *args):
    print ("formal arg:", farg)
    for arg in args:
        print ("another arg:", arg)

test_var_args(1, "two", 3)


def test_var_kwargs(farg, **kwargs):
    print ("formal arg:", farg)
    for key in kwargs:
        print ("another keyword arg: %s: %s" % (key, kwargs[key]))

test_var_kwargs(farg=1, myarg2="two", myarg3=3)



# Using *args and **kwargs when calling a function

def test_var_args_call(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

test_var_args_call (1,"two",3)

args = (1,"two", 3)
test_var_args_call(*args)


def test_var_args_call(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

kwargs = {"arg1": 1,"arg3": 3, "arg2": "two"}

test_var_args_call(**kwargs)



"""
Introduce the concept of Global and Local Variables
"""

# Global variables are the one that are defined and 
# declared outside a function and we need to use them inside a function.


# This function uses global variable s 
def f():  
    print (s)  
  
# Global scope 
s = "I love Forsk Technologies"
f() 


# If a variable with same name is defined inside the scope of function as well 
# then it will print the value given inside the function only and not the global value.



# This function has a variable with 
# name same as s. 
def f():  
    s = "Me too."
    print (s)  
  
# Global scope 
s = "I love Forsk Technologies" 
f() 
print ( s )


# Ambiguty Code 
def f():  
    print (s) 
  
    # This program will NOT show error 
    # if we comment below line.  
    s = "Me too."
  
    print ( s )
  
# Global scope 
s = "I love Forsk Technologies" 
f() 
print  ( s )


# Correct Code

# This function modifies global variable 's' 
def f(): 
    global s 
    print ( s )
    s = "I love Forsk Technologies"
    print (s)  
  
# Global Scope 
s = "Python is great!" 
f() 
print (s) 



a = 1
  
# Uses global because there is no local 'a' 
def f(): 
    print ('Inside f() : ', a) 
  
# Variable 'a' is redefined as a local 
def g():     
    a = 2
    print ('Inside g() : ',a )
  
# Uses global keyword to modify global 'a' 
def h():     
    global a 
    a = 3
    print ('Inside h() : ',a) 
  
# Global scope 
print ('global : ',a) 
f() 
print ('global : ',a) 
g() 
print ('global : ',a) 
h() 
print ('global : ',a) 



# Formatted Output
# https://www.python-course.eu/python3_formatted_output.php





# Add some topics for Data Structure and Searching and Sorting Algorithms
  
