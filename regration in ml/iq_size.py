# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:39:35 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
dataset=pd.read_csv("iq_size.csv")
features=dataset.iloc[:,1:4].values
labels=dataset.iloc[:,0].values
from sklearn.model_selection import train_test_split
features_test,features_train,labels_test,labels_train=train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
regressor.predict(features_test)

x=np.array[0,90,70,150]
print(regressor.predict(x))


regressor.score(features_test,labels_test)
regressor.score(features_train,labels_train)
print(regressor.coef_)
import statsmodels.formula.api as sm
features=np.append(arr=np.ones((38,1)),values=features,axis=1)
features_opt=features[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
features_opt=features[:,[1,2]]
regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
regressor_OLS.summary()
#index 1 brain size is important for predict intelligence.