# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:25:34 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("bluegills.csv")
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values
from sklearn.linear_model import LinearRegression
linreg=LinearRegression()
linreg.fit(features,labels)
linreg.predict(3)
linreg.score(features,labels)

from sklearn.preprocessing import PolynomialFeatures
poly_obj=PolynomialFeatures(degree=5)
features_poly=poly_obj.fit_transform(features)
linreg2=LinearRegression()
linreg2.fit(features_poly,labels)
print(linreg2.predict(poly_obj.fit_transform(3)))
linreg2.score(features_poly,labels)

feat_grid = np.arange(min(features),max(features),0.1).reshape(-1,1)
plt.scatter(features,labels,color="red")
plt.plot(feat_grid,linreg2.predict(poly_obj.fit_transform(feat_grid)),color="blue")
plt.xlabel("age")
plt.ylabel("length")
plt.title("age vs length")
linreg2.score(poly_obj.fit_transform(features), labels)
