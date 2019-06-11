#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:10:48 2018

@author: Forsk
"""

#Example 1

# A 2-dimensional array of size 2 x 3, composed of 4-byte integer elements:
import numpy as np


x = np.array([[1, 2, 3], [4, 5, 6]], dtype = 'int32')

print (type(x))
print (x.shape)
print (x.dtype)

"""
https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference

"""


#-----------------------------------------------------------------------------
# Numpy supports all data types likes bool, integer, float, complex etc.
# They are defined by the numpy.dtype class 

import numpy as np 

x = np.float32(1.0) 
x = np.float64(1.0)
x = np.float_(1.0)
print (x) 

y = np.array([1,2,4]) 
print (y) 



z = np.arange(20, dtype = np.uint8)


print (z)
print (z.dtype)


#----------------------------------------------------------------------------
"""
There are a couple of mechanisms for creating arrays in NumPy:
 a. Conversion from other Python structures (e.g., lists, tuples).
 b. Built-in NumPy array creation (e.g., arange, ones, zeros, etc.).
 c. Reading arrays from disk, either from standard or custom formats 
     (e.g. reading in from a CSV file).
"""

import numpy as np
# Converting an python list to ndarray
x = np.array([2,3,1,0])
print (x)
# Converting an python tuple to ndarray
x = np.array((1, 2,3))
print (x)
print(x.dtype  )
# ndarray builtin functions
# create array from scratch

# zeros(shape) -- creates an array filled with 0 values with the specified 
#                  shape. The default dtype is float64.
x = np.zeros((2,3), dtype=np.int8)
print (x)


# ones(shape) -- creates an array filled with 1 values. 

x = np.ones((2,3), dtype="int8" )
print (x)

# arange() -- creates arrays with regularly incrementing values.

print (np.arange(10)) 

#-----------------------------------------------------------------------
# linspace() -- creates arrays with a specified number of elements, 
#and spaced equally between the specified beginning and end values.

x = np.linspace(1, 4, 20)
print (x)

#np.around(x,2)



#random.random(shape) – creates arrays with random floats over the interval [0,1].
print (np.random.random((2,3))*100)




# Printing Arrays
import numpy as np 
a = np.arange(9) 
print (a) 

#reshaping it another shape
b = a.reshape(3,3) 
print (b)                                                                      

#another example of reshaping
c = np.arange(8).reshape(2,2,2) 
print (c)

#-------------------------------------------------------------------------
"""
Arrays Operations - Basic operations apply element-wise. 
The result is a new array with the resultant elements.
Operations like *= and += will modify the existing array.
"""

import numpy as np
a = np.arange(5) 
b = np.arange(5) 




print (a+b) 

print (a-b)

print (a**3)

print (a>3)

print (np.sin(a)) 



print (a*b) 

#--------------------------------------------------------------------
#Linear Algebra functions are also available

# Matrices
A = np.mat('1.0 2.0; 3.0 4.0') 
print(A)

X = np.mat('5.0 7.0') 
Y = X.T
 

print (np.linalg.solve(A, Y)) # solving linear equation 

#----------------------------------------
#How to check for library version
import numpy as np
print (np.__version__)

#---------------------------------------
# -*- coding: utf-8 -*-

"""
Mean, Median, Mode, and introducing NumPy

Mean vs. Median

Let's create some fake income data, centered around 27,000 
with a normal distribution and standard deviation of 15,000, with 10,000 data points. 
Then, compute the mean (average)
    
"""

import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
print(type(incomes))
np.mean(incomes)
np.median(incomes)
np.std(incomes)

#We can segment the income data into 50 buckets, and plot it as a histogram:

import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()

#box and whisker plot to show distribution
#https://chartio.com/resources/tutorials/what-is-a-box-plot/

incomes = np.append(incomes,100000000)
plot = plt.boxplot(incomes)

"""
fliers = plot['fliers']

# Iterate over it!
for fly in fliers:
    fdata = fly.get_data()
    fly.set_data([fdata[0][0],fdata[0][-1]],[fdata[1][0],fdata[1][-1]])


[item.get_ydata()[0] for item in plot['whiskers']]
"""

#second version

import pandas as pd
_,bp = pd.DataFrame.boxplot(pd.DataFrame(incomes), return_type='both')

outliers = [flier.get_ydata() for flier in bp["fliers"]]
boxes = [box.get_ydata() for box in bp["boxes"]]
medians = [median.get_ydata() for median in bp["medians"]]
whiskers = [whiskers.get_ydata() for whiskers in bp["whiskers"]]
#Computing Median
np.median(incomes)

#Computing Mean

np.mean(incomes)



#Adding Bill Gates into the mix. income inequality!(Outliers)

incomes = np.append(incomes, [1000000])


#Median Remains Almost SAME
np.median(incomes)


#Mean Changes distinctly

np.mean(incomes)

plt.plot(incomes[:100])

#---------------------------------------
#Standard Deviation

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
#incomes = np.random.normal(27000.0, 15000.0, 10000)
plt.hist(incomes, 50)
plt.show()

print (incomes.std())
print (incomes.var())
#The standard deviation is the square root of the variance. 


randNumbers = np.random.randint(5,15,40)
counts = np.bincount(randNumbers)
print(counts)
print (np.argmax(counts))
print (np.argmin(counts))



#################


from numpy import genfromtxt
#to read as record array
my_data = genfromtxt('Salaries.csv', delimiter=',', dtype=None)



###################





#------------------------More Numpy--------------------#
# np.identity() to create a square 2d array with 1's across the diagonal

import numpy as np
np.identity(n = 4)      # Size of the array

# np.eye() to create a 2d array with 1's across a specified diagonal

np.eye(N = 3,  # Number of rows
       M = 5,  # Number of columns
       k = 0)  # Index of the diagonal (main diagonal (0) is default)

one_d_array = np.array([1,2,3,4,5,6])
print(one_d_array)
# Create a new 2d array
two_d_array = np.array([one_d_array, one_d_array + 6, one_d_array + 12])
print(two_d_array)
# Slice elements starting at row 2, and column 5

two_d_array[1:, 4:]

# Reverse both dimensions (180 degree rotation)

two_d_array[::-1]
two_d_array[:,::-1]
two_d_array[::-1, ::-1]

#Reshaping an Array
np.reshape(a=two_d_array,        # Array to reshape
           newshape=(6,3)) 

temp = np.reshape(a=two_d_array,        # Array to reshape
           newshape=(3,3,2)) 
print(temp)      # Dimensions of the new array

#Unravel a multi-dimensional into 1 dimension with np.ravel():
np.ravel(a=two_d_array,
         order='C')         # Use C-style unraveling (by rows)

np.ravel(a=two_d_array,
         order='F')         # Use Fortran-style unraveling (by columns)


#Alternatively, use ndarray.flatten() to flatten a multi-dimensional into 1 dimension and return a copy of the result:
two_d_array.flatten()


#Transpose of the array
two_d_array.T


#Flip an array vertically np.flipud(), upside down :

np.flipud(two_d_array)

  
#Flip an array horizontally with np.fliplr(), left to right:

np.fliplr(two_d_array)


#Rotate an array 90 degrees counter-clockwise with np.rot90():
np.rot90(two_d_array,
         k=2)             # Number of 90 degree rotations

#Shift elements in an array along a given dimension with np.roll():
np.roll(a= two_d_array,
        shift =2,        # Shift elements 2 positions
        axis = 1)         # In each row

np.roll(a= two_d_array,
        shift = 2,        # Shift elements 2 positions
        axis = 0)         # In each columns

#Join arrays along an axis with np.concatenate():
array_to_join = np.array([[10,20,30],[40,50,60],[70,80,90]])

np.concatenate( (two_d_array.T,array_to_join),  # Arrays to join
               axis=0)

np.concatenate( (two_d_array,array_to_join),  # Arrays to join
               axis=1)                        # Axis to join upon


# Get the mean of all the elements in an array with np.mean()

np.mean(two_d_array)

# Provide an axis argument to get means across a dimension

np.mean(two_d_array,
        axis = 1)     # Get means of each row

# Get the standard deviation all the elements in an array with np.std()

np.std(two_d_array)


# Provide an axis argument to get standard deviations across a dimension

np.std(two_d_array,
        axis = 0)     # Get stdev for each column

# Sum the elements of an array across an axis with np.sum()

np.sum(two_d_array, 
       axis=1)        # Get the row sums

np.sum(two_d_array,
       axis=0)        # Get the column sums

# Take the square root of each element with np.sqrt()

np.sqrt(two_d_array)

"""
Take the dot product of two arrays with np.dot(). 
This function performs an element-wise multiply and then a sum for 1-dimensional arrays (vectors) and matrix multiplication for 2-dimensional arrays.
"""

# Take the vector dot product of row 0 and row 1

np.dot(two_d_array[0,0:],  # Slice row 0
       two_d_array[1,0:])  # Slice row 1


np.multiply(two_d_array[0,0:],  # Slice row 0
       two_d_array[1,0:])
-------------------------------------------------------------------------------------------------------------------------------------------------
