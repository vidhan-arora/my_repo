# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:32:04 2019

@author: lenovo


There are two categories: Pos (reviews that express a positive or favorable sentiment) 
and Neg (reviews that express a negative or unfavorable sentiment). For this assignment,
 we will assume that all reviews are either positive or negative; there are no neutral reviews.

Perform sentiment analysis on the text reviews to determine whether its positive or
 negative and build confusion matrix to determine the accuracy
 """
 
import pandas as pd
import numpy as np
import matpoltlib.pyplot as plt
dataset=pd.read_csv("movie.csv")

import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,2000):
    text = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    text = text.lower()
    text = text.split()
    text = [word for word in text if not word in set(stopwords.words('english'))]
    ps=PorterStemmer()
    text=[ps.stem(word) for word in text]
    text=' '.join(text)
    corpus.append(text)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
dataset["class"]=np.where(dataset["class"]=="Pos",0,1)
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, dataset["class"], test_size = 0.20, random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
classifier.score(features_test,labels_test)
#==================================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("movie.csv")
from sklearn.naive_bayes import GaussianNB,BernoulliNB,MultinomialNB
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0,2000):
    text = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
    text = text.lower()
    text = text.split()
    text = [word for word in text if  word not in set(stopwords.words('english'))]
    ps=PorterStemmer()
    text=[ps.stem(word) for word in text]
    text=' '.join(text)
    corpus.append(text)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
dataset["class"]=np.where(dataset["class"]=="Pos",0,1)
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, dataset["class"], test_size = 0.20, random_state = 0)

gnb=GaussianNB()

gnb.fit(features_train,labels_train)
        
label_pred=gnb.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_gnb=confusion_matrix(labels_test,label_pred)
gnb.score(features_test,labels_test)
#===============================================================================
bnb=BernoulliNB()

bnb.fit(features_train,labels_train)
        
label_pred=bnb.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_bnb=confusion_matrix(labels_test,label_pred)
bnb.score(features_test,labels_test)
 #===============================================================================
mnb=MultinomialNB()

mnb.fit(features_train,labels_train)
        
label_pred=mnb.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_mnb=confusion_matrix(labels_test,label_pred)
mnb.score(features_test,labels_test) 
#for this question multinomial is  best.