# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:45:09 2019

@author: lenovo
"""

Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                                     ----> represented by column B.
Uniformity of Cell Size(1 - 10)                             ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                        ----> represented by column D.
Marginal Adhesion (1 - 10)                                  ----> represented by column E.
Single Epithelial Cell Size (1 - 10)                        ----> represented by column F.
Bare Nuclei (1 - 10)                                               ----> represented by column G.
Bland Chromatin (1 - 10)                                     ----> represented by column H.
Normal Nucleoli (1 - 10)                                      ----> represented by column I.
Mitoses (1 - 10)                                                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.
Impute the missing values with the most frequent values.
Perform Classification on the given data-set to predict if the tumor is cancerous or not.
Check the accuracy of the model.Predict whether a women has Benign tumor or Malignant tumor,
 if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5,
 Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2
 and Single Epithelial Cell Size is 2
(you can neglect the id number column as it doesn't seem  a predictor column)
-------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
dataset=pd.read_csv("breast_cancer.csv")
dataset=dataset.fillna(method='ffill')
dataset=dataset[["A","B","C","D","E","F","G","H","I","J","K"]]
from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(dataset, test_size=0.2, random_state=0)
#for GaussianNB
gnb=GaussianNB()
used_features=["A","B","C","D","E","F","G","H","I","J"]
gnb.fit(features_train[used_features].values,features_train["K"].values)
label_pred=gnb.predict(features_test[used_features])
from sklearn.metrics import confusion_matrix
cm_gnb=confusion_matrix(features_test["K"],label_pred)
x=([0,6,2,5,3,2,7,9,2,4])
x=np.array(x).reshape(1,-1)
x=pred=gnb.predict(x)#after prediction on this we find it was not a data of cancerous tumor.
#for multinomialNB
mnb= MultinomialNB()
used_features=["A","B","C","D","E","F","H","I","J"]
mnb.fit(features_train[used_features].values,features_train["K"].values)
label_pred=mnb.predict(features_test[used_features])
from sklearn.metrics import confusion_matrix
cm_mnb=confusion_matrix(features_test["K"],label_pred)
#for bernoulliNB
bnb= BernoulliNB()
used_features=["A","B","C","D","E","F","H","I","J"]
bnb.fit(features_train[used_features].values,features_train["K"].values)
label_pred=bnb.predict(features_test[used_features])
from sklearn.metrics import confusion_matrix
cm_bnb=confusion_matrix(features_test["K"],label_pred)

#mnb was best for this code challange.


















