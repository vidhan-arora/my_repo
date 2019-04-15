# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:29:20 2019

@author: lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("foodtruck.csv")
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values
#train test split use for big data handling
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
regressor.predict(features_test)
print(regressor.predict(3.03))
#visulisation 
plt.scatter(features_train,labels_train,color="blue")
plt.plot(features_train,regressor.predict(features_train),color="red")
plt.xlabel("population")
plt.ylabel("profit")
plt.title("food_truck_chart")
plt.show()
plt.scatter(features_test,labels_test,color="blue")
plt.plot(features_train,regressor.predict(features_train),color="red")
plt.xlabel("population")
plt.ylabel("profit")
plt.title("food_truck_chart")
plt.show()
print(regressor.score(features_train,labels_train)) 
print(regressor.score(features_test,labels_test)) 



