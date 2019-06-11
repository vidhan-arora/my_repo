# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:40:54 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
dataset=pd.read_csv("mushrooms.csv")
features=dataset.iloc[:,[5,21,22]].values
labels=dataset.iloc[:,0].values
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features[:, 0] = labelencoder.fit_transform(features[:, 0])



from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features[:, 1] = labelencoder.fit_transform(features[:, 1])


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder() 
features[:, 2] = labelencoder.fit_transform(features[:, 2])


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
features = onehotencoder.fit_transform(features).toarray()

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [1])
features = onehotencoder.fit_transform(features).toarray()

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [2])
features = onehotencoder.fit_transform(features).toarray()



from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)
#features_test=sc.transform(features_test)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(features,labels)

labels_pred=classifier.predict(features)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels,labels_pred)