# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

# Importing dataset
data = pd.read_csv("training_titanic.csv")

# Convert categorical variable to numeric
data["Sex_cleaned"]=np.where(data["Sex"]=="male",0,1)
data["Embarked_cleaned"]=np.where(data["Embarked"]=="S",0,
                                  np.where(data["Embarked"]=="C",1,
                                           np.where(data["Embarked"]=="Q",2,3)
                                          )
                                 )
# Cleaning dataset of NaN
data=data[[
    
    "Fare",
    "Survived"

]].dropna(axis=0, how='any')

"""
data=data[[
    "Survived",
    "Pclass",
    "Sex_cleaned",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked_cleaned"
]].dropna(axis=0, how='any')

"""

# Split dataset in training and test datasets
from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(data, test_size=0.5, random_state=0)


gnb = GaussianNB()
used_features =[

    "Fare",
   
]

# Train classifier
gnb.fit(
    features_train[used_features].values,
    features_train["Survived"].values
)
labels_pred = gnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(features_test["Survived"], labels_pred)










mnb = MultinomialNB()
used_features =[  
    "Fare",
   
]

# Train classifier
mnb.fit(
    features_train[used_features].values,
    features_train["Survived"].values
)
labels_pred = mnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_mnb = confusion_matrix(features_test["Survived"], labels_pred)


bnb = BernoulliNB()
used_features =[
   
    "Fare",
  
]

# Train classifier
bnb.fit(
    features_train[used_features].values,
    features_train["Survived"]
)
labels_pred = bnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_bnb = confusion_matrix(features_test["Survived"], labels_pred)


"""
Bernoulli Naive Bayes : It assumes that all our features are binary such that they take only two values. Means 0s can represent “word does not occur in the document” and 1s as "word occurs in the document". Email classifier .

Multinomial Naive Bayes : Its is used when we have discrete data (e.g. movie ratings ranging 1 and 5 as each rating will have certain frequency to represent). In text learning we have the count of each word to predict the class or label.

Gaussian Naive Bayes : Because of the assumption of the normal distribution, Gaussian Naive Bayes is used in cases when all our features are continuous. For example in Iris dataset features are sepal width, petal width, sepal length, petal length. So its features can have different values in data set as width and length can vary. We can’t represent features in terms of their occurrences. This means data is continuous. Hence we use Gaussian Naive Bayes here.

"""

"""
http://kenzotakahashi.github.io/naive-bayes-from-scratch-in-python.html
https://nlp.stanford.edu/IR-book/
https://blog.sicara.com/naive-bayes-classifier-sklearn-python-example-tips-42d100429e44
https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn
Naive Bayes Explainer in the email(forsklabs)

"""
