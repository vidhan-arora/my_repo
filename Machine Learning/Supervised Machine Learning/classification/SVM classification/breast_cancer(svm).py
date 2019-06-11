# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:42:34 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("breast_cancer.csv")
dataset=dataset.fillna(method='ffill')
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1]
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.svm import SVC
classifier = SVC( kernel = 'poly',random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)