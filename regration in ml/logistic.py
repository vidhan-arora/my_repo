# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:54:13 2019

@author: lenovo
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv("affairs.csv")
features=dataset.iloc[:,0:8]
labels=dataset.iloc[:,-1]

from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(categorical_features=[6,7])
features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]



from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)

x=[3,25,3,1,4,16,2,2]
x=np.array(x)
classifier.predict(x.reshape(1,-1))


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
score.cm(labels_test,labels_pred)