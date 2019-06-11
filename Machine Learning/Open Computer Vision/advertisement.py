# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:44:50 2019

@author: lenovo
"""

import pandas as pd
train_data=pd.read_json("train_data.json",lines=True)
test_data=pd.read_json("test_data.json",lines=True)




import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer



corpus = []

for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', train_data["heading"][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()


corpus1 = []

for i in range(0, 15370):
    review = re.sub('[^a-zA-Z]', ' ', test_data["heading"][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus1.append(review)
features2 = cv.transform(corpus1).toarray()




features_train_data=train_data.iloc[:,[1,3]].values
labels_train_data=train_data.iloc[:,0].values
features_test_data=test_data.iloc[:,[0,2]].values

le_objs = []

from sklearn.preprocessing import LabelEncoder
for i in range(features_train_data.shape[1]):
    labelencoder = LabelEncoder()
    features_train_data[:, i] = labelencoder.fit_transform(features_train_data[:, i])
    le_objs.append(labelencoder)

le_labels = LabelEncoder()
labels_train_data = le_labels.fit_transform(labels_train_data)


for col, obj in zip(range(features_train_data.shape[1]),le_objs):
    features_test_data[:, col] = obj.transform(features_test_data[:, col])


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = "all")
features_train_data = onehotencoder.fit_transform(features_train_data).toarray()

features_test_data = onehotencoder.transform(features_test_data).toarray()

import numpy as np

features_train_data = np.append(arr=features,values=features_train_data,axis=1)
features_test_data = np.append(arr=features2,values=features_test_data,axis=1)


from sklearn.model_selection import train_test_split as TTS
f_train,f_test,l_train,l_test = TTS(features_train_data,labels_train_data,test_size=0.3, 
                                    random_state=0)

model_scores = {}

from sklearn.decomposition import PCA
pca = PCA(n_components = 10)
f_train = pca.fit_transform(f_train)
f_test = pca.transform(f_test)
explained_variance = pca.explained_variance_ratio_

from sklearn.metrics import accuracy_score

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(f_train, l_train)
nb_pred = nb.predict(f_test)
nb_score = accuracy_score(l_test,nb_pred)
model_scores["Naive Bayes"] = nb_score


# SVM
from sklearn.svm import SVC
svm = SVC( kernel = 'linear',random_state = 0)
svm.fit(f_train, l_train)
svm_pred = svm.predict(f_test)
svm_score = accuracy_score(l_test,svm_pred)
model_scores["SVM"] = svm_score

# KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(f_train,l_train)
knn_pred = knn.predict(f_test)
knn_score = accuracy_score(l_test,knn_pred)

model_scores["KNN"]=knn_score

# RandomForest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=70, random_state=0)
rf.fit(f_train,l_train)
rf_pred = rf.predict(f_test)
rf_score = accuracy_score(l_test,rf_pred)
model_scores["RandomForest"] = rf_score


final_test_data = pca.transform(features_test_data)
final_pred = rf.predict(final_test_data)
final_labels = pd.DataFrame(le_labels.inverse_transform(final_pred))