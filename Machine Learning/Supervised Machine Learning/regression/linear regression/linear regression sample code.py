# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:18:18 2019

@author: lenovo
"""

SIMPLE LINEAR REGRESSION


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Income_Data.csv')

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

"""
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test 
= train_test_split
(features, labels, test_size = 0.2,
                   random_state = 0)

"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(features, labels)

regressor.predict(6.5)


# Predicting the Test set results
labels_pred = regressor.predict(features_test)

print (regressor.predict(6.5))

# Visualising the Training set results
plt.scatter(features_train, labels_train, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience (Training set)')
plt.xlabel('ML-Experience')
plt.ylabel('Income')
plt.show()


# Visualising the Test set results
#plt.scatter(features_train, labels_train, color = 'green')
plt.scatter(features_test, labels_test, color = 'red')
plt.plot(features_train, regressor.predict(features_train), color = 'blue')
plt.title('Income vs ML-Experience (Test set)')
plt.xlabel('ML-Experience')
plt.ylabel('Income')
plt.show()



#Model accuracy
print (regressor.score(features_test, labels_test))
print (regressor.score(features_train, labels_train))


CODE CHALLENGES

Q1. (Create a program that fulfills the following specification.)
Foodtruck.csv


You will implement linear regression to predict the profits for a food chain company.

Case: Suppose you are the CEO of a restaurant franchise and are considering 
different cities for opening a new outlet. 
The chain already has food-trucks in various cities and you have data for profits 
and populations from the cities. 
You would like to use this data to help you select which city to expand to next. 

Foodtruck.csv contains the dataset for our linear regression problem. 
The first column is the population of a city and the second column is the 
profit of a food truck in that city. 
A negative value for profit indicates a loss.

Perform Simple Linear regression to predict the profit based on the population 
observed and visualize the result.
Based on the above trained results, what will be your estimated profit, 
if you set up your outlet in Jaipur? (Current population in Jaipur is 3.073 million)



Q2. (Create a program that fulfills the following specification.)

Import Bahubali2vsDangal.csv file.

It contains Data of Day wise collections of the movies Bahubali 2 and Dangal (in crores) for the first 9 days.
Now, you have to write a python code to predict which movie would collect more on the 10th day.
