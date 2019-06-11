# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:20:56 2019

@author: lenovo
"""

POLYNOMIAL REGRESSION


# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
features = dataset.iloc[:, 1:2].values
labels = dataset.iloc[:, 2].values


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features, labels)

print ("Predicting result with Linear Regression",)
print (lin_reg.predict(6.5))

#print the scores
print lin_reg.score(features, labels)
#if the score is poor, it seems we are using a very simple model that does 
#not fit the data well. May be a case of underfitting


# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg.predict(features), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()



# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
# create the polynomial features using above class
poln_object = PolynomialFeatures(degree = 6)

features_poln = poln_object.fit_transform(features)
#poln_object.fit(features_poln)

#once you have the poln_matrix read, input it to linear regressor
lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poln, labels)




print ("Predicting result with Polynomial Regression",)
#need to convert 6.5 into polynomial features
#poln_object.fit_transform(6.5)
#pd.DataFrame(poln_object.fit_transform(6.5))

print (lin_reg_2.predict(poln_object.fit_transform(6.5)))



# Visualising the Polynomial Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_2.predict(poln_object.fit_transform(features)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#evaluate the score
#you will have to convert features to polynomial matrix and then get the score
lin_reg_2.score(poln_object.fit_transform(features), labels)




# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
features_grid = np.arange(min(features), max(features), 0.1)
features_grid = features_grid.reshape((-1, 1))
plt.scatter(features, labels, color = 'red')
plt.plot(features_grid, lin_reg_2.predict(poln_object.fit_transform(features_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

CODE CHALLENGE


Q1. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.



