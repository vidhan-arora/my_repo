# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:18:25 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset1=pd.read_csv("train.csv")
dataset2=pd.read_csv("test.csv")
features_dataset1=dataset1.iloc[:,:-1].values
labels_dataset1=dataset1.iloc[:,-1].values
features_dataset2=dataset2.iloc[:,:-1].values
labels_dataset2=dataset2.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels_dataset1 = labelencoder.fit_transform(labels_dataset1)
labelencoder = LabelEncoder()
labels_dataset2 = labelencoder.fit_transform(labels_dataset2)
#===============================================================================
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_dataset1, labels_dataset1)
labels_pred = classifier.predict(features_dataset2)
from sklearn.metrics import confusion_matrix  
cm=(confusion_matrix(labels_dataset2, labels_pred))  
print(cm)
score=classifier.score(features_dataset1,labels_dataset1)
score1=classifier.score(features_dataset2,labels_dataset2)
#==============================================================================
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_dataset1, labels_dataset1)  
labels_pred = classifier.predict(features_dataset2) 
from sklearn.metrics import confusion_matrix  
cm=(confusion_matrix(labels_dataset2, labels_pred))  
print(cm)
score=classifier.score(features_dataset1,labels_dataset1)
print(score)
score1=classifier.score(features_dataset2,labels_dataset2) 
print(score1)
#===============================================================================
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_dataset1,labels_dataset1)
labels_pred=classifier.predict(features_dataset2)
from sklearn.metrics import confusion_matrix  
cm=(confusion_matrix(labels_dataset2, labels_pred))  
print(cm)
score=classifier.score(features_dataset1,labels_dataset1)
print(score)
score1=classifier.score(features_dataset2,labels_dataset2) 
print(score1)
#===============================================================================
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(features_dataset1,labels_dataset1)
labels_pred=classifier.predict(features_dataset2)
from sklearn.metrics import confusion_matrix
cm=(confusion_matrix(labels_dataset2, labels_pred))  
print(cm)
score=classifier.score(features_dataset1,labels_dataset1)
print(score)
score1=classifier.score(features_dataset2,labels_dataset2) 
print(score1)

import statsmodels.formula.api as sm
#This is done because statsmodels library requires it to be done for constants.
features_dataset1 = np.append(arr = np.ones((features_dataset1.shape[0], 1)), values = features_dataset1, axis = 1)
cols = list(range(features_dataset1.shape[1]))
while (True):
    features_opt = features_dataset1[:, cols]
    classifier_OLS = sm.OLS(endog = labels_dataset1,exog =features_opt).fit()
    p_values = classifier_OLS.pvalues
    if p_values.max() < 0.05 :
            # deleting a whole column if required that's why 3rd parameter is 1 means axis=1
            print(classifier_OLS.summary())
            break
    else:
        val = list(p_values).index(p_values.max())
        cols.pop(val)
    print("Executing...")

features_test_opt = features_dataset2[:,cols]                                  




