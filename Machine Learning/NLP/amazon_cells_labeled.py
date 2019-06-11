# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:45:07 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("amazon_cells_labelled.txt",delimiter="\t",header=None)
from sklearn.naive_bayes import GaussianNB,BernoulliNB,MultinomialNB
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,1000):
    text = re.sub('[^a-zA-Z]', ' ', dataset[0][i])
    text = text.lower()
    text = text.split()
    text = [word for word in text if  word not in set(stopwords.words('english'))]
    ps=PorterStemmer()
    text=[ps.stem(word) for word in text]
    text=' '.join(text)
    corpus.append(text)
#with the help of count vectorizer in this we describe how much data out of total 
#we take in features for eg in thid we take 1500 data out of 2000
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values
#dataset[0]=np.where(dataset[0]=="Pos",0,1)
#in this portion we split training and testing data.
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)
#in this we will apply gaussian naive bayes.
gnb=GaussianNB()

gnb.fit(features_train,labels_train)
        
label_pred=gnb.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_gnb=confusion_matrix(labels_test,label_pred)
gnb1=gnb.score(features_test,labels_test)
print(gnb1)

from sklearn.svm import SVC
classifier = SVC( kernel = 'rbf',random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)