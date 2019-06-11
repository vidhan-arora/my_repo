# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:57:43 2019

@author: lenovo
"""

Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", 
    "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two 
    is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 
    6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower 
    engine giving it a displacement of about 215. (Give the prediction from both the models)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Auto_mpg.txt",delimiter="\s+",header=None)
dataset.columns=([ "mpg", "cylinders", "displacement","horsepower","weight","acceleration", 
    "model year", "origin", "car name"])
dataset.groupby(["mpg","car name"]).max()
features=dataset.iloc[:,1:8]
labels=dataset.iloc[:,0]
features["horsepower"]=features["horsepower"].replace("?",100)
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor()
regressor.fit(features_train,labels_train)
labels_pred=regressor.predict(features_test)
df=pd.DataFrame({"actual":labels_test,"predicted":labels_pred})
print(df)
x=([6,215,100,2630,22.2,80,3])
x=np.array(x).reshape(1,-1)
regressor1=regressor.predict(x)

















