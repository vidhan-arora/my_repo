# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:13:19 2019

@author: lenovo
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate
    your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4,
    went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, 
    didn't went to any top-tire school, having Master's Degree with Internship.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("PastHires.csv")
features=df.iloc[:,:-1]
labels=df.iloc[:,-1]
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features["Level of Education"] = labelencoder.fit_transform(features["Level of Education"])
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features["Employed?"] = labelencoder.fit_transform(features["Employed?"])
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features["Top-tier school"] = labelencoder.fit_transform(features["Top-tier school"])
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features["Interned"] = labelencoder.fit_transform(features["Interned"])
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
labels=labelencoder.fit_transform(labels)
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2,random_state=0)  

#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

#Evaluating score
#For classification tasks some commonly used metrics are confusion matrix, precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix  
cm=(confusion_matrix(labels_test, labels_pred))  












