# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:06:04 2019

@author: lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("Bahubali2_vs_Dangal.csv")
features=dataset.iloc[:,0].values.reshape(-1,1)
labels=dataset.iloc[:,1:3].values


#from sklearn.model_selection import train_test_split
#features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)
#

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features,labels)
print(regressor.predict(10))


plt.scatter(features,labels[:,0],color="red")
plt.plot(features,regressor.predict(features),color="blue")
plt.title("movie collection")
plt.xlabels("bahubali",label="line1")
plt.ylabels("dangal",label="line2")
plt.show()
plt.legend()
plt.scatter(features,labels[:,0],color="red")
plt.scatter(features,labels[:,1],color="blue")
plt.plot(features,regressor.predict(features),color="blue")
plt.title("movie collection")
plt.xlabels("bahubali",label="line1")
plt.ylabels("dangal",label="line2")
plt.show()
plt.legend()
print(regressor.score(features,labels))
