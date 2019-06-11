# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:39:35 2019

@author: lenovo
"""
CODE CHALLENGES


Q1. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.



import pandas as pd
import numpy as np
dataset=pd.read_csv("iq_size.csv")
features=dataset.iloc[:,1:4].values
labels=dataset.iloc[:,0].values
from sklearn.model_selection import train_test_split
features_test,features_train,labels_test,labels_train=train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
regressor.predict(features_test)

x=np.array[0,90,70,150]
print(regressor.predict(x))


regressor.score(features_test,labels_test)
regressor.score(features_train,labels_train)
print(regressor.coef_)
import statsmodels.formula.api as sm
features=np.append(arr=np.ones((38,1)),values=features,axis=1)
features_opt=features[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
#index 1 brain size is important for predict intelligence.