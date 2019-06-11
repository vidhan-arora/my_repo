# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:35:06 2019

@author: vidhan
"""
!python -m pip install --upgrade pip
!pip install mysql-connector-python
import mysql.connector as mcon

con = mcon.connect(username="vidhanarora", password="vidhan1234",host="db4free.net", db="vidhan")

query = "select * from online_marketing"
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_sql(query, con)
dataset.isnull().any(axis=1)
dataset.describe()
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 1] = labelencoder.fit_transform(features[:, 1])
labelencoder = LabelEncoder()
features[:, 2] = labelencoder.fit_transform(features[:, 2])
labelencoder = LabelEncoder()
features[:, 3] = labelencoder.fit_transform(features[:, 3])
labelencoder = LabelEncoder()
features[:, 4] = labelencoder.fit_transform(features[:, 4])
labelencoder = LabelEncoder()
features[:, 6] = labelencoder.fit_transform(features[:, 6])
labelencoder = LabelEncoder()
features[:, 7] = labelencoder.fit_transform(features[:, 7])
labelencoder = LabelEncoder()
features[:, 8] = labelencoder.fit_transform(features[:, 8])
labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [1,2,3,4,6,7,8])
features = onehotencoder.fit_transform(features).toarray()
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test) 

#RANDOMFOREST##################################################################
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=40, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
score=classifier.score(features_train,labels_train)
score_random1=classifier.score(features_test,labels_test)  
print(score_random1)     


#SVM###########################################################################
from sklearn.svm import SVC
classifier = SVC( kernel = 'poly',random_state = 0)
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
score=classifier.score(features_train,labels_train)
score_svm1=classifier.score(features_test,labels_test) 
print(score_svm1)
#KNN#########################################################################
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(features,labels)
labels_pred=classifier.predict(features)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels,labels_pred)
score=classifier.score(features_train,labels_train)
scoreknn1=classifier.score(features_test,labels_test)
print(scoreknn1) 
#logistic###################################################################
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
score=classifier.score(features_train,labels_train)
scorelogistic1=classifier.score(features_test,labels_test) 
print(scorelogistic1)
import matplotlib.pyplot as plt
plt.bar(["random","svm","knn","logistic"],[score_random1,score_svm1,scoreknn1,scorelogistic1],align="center",alpha=0.5)
plt.title("score card")
plt.xlabel("classification_model")
plt.ylabel("score")
plt.show()

                      




