# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:25:34 2019

@author: lenovo
"""
CODE CHALLENGE


Q1. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fishture?)
    What is the length of a randomly selected five-year-old bluegill fish? Perfor

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nam polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("bluegills.csv")
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values
from sklearn.linear_model import LinearRegression
linreg=LinearRegression()
linreg.fit(features,labels)
linreg.predict(5)
linreg.score(features,labels)

from sklearn.preprocessing import PolynomialFeatures
poly_obj=PolynomialFeatures(degree=5)
features_poly=poly_obj.fit_transform(features)
linreg2=LinearRegression()
linreg2.fit(features_poly,labels)
print(linreg2.predict(poly_obj.fit_transform(3)))
linreg2.score(features_poly,labels)

feat_grid = np.arange(min(features),max(features),0.1).reshape(-1,1)
plt.scatter(features,labels,color="red")
plt.plot(feat_grid,linreg2.predict(poly_obj.fit_transform(feat_grid)),color="blue")
plt.xlabel("age")
plt.ylabel("length")
plt.title("age vs length")
linreg2.score(poly_obj.fit_transform(features), labels)
