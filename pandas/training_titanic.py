# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:32:46 2019

@author: lenovo
"""

import pandas as pd
df=pd.read_csv("training_titanic.csv")
print(df["Survived"].value_counts())
df_survive = df["Survived"][df["Survived"]==0].value_counts()
print(df_survive)
df["Survived"].describe()
df["Survived"][(df["Survived"]==0) & (df["Sex"]=="male")].value_counts()
df["Survived"][(df["Survived"]==1) & (df["Sex"]=="male")].value_counts()
df["Survived"][(df["Survived"]==0) & (df["Sex"]=="female")].value_counts()
df["Survived"][(df["Survived"]==1) & (df["Sex"]=="female")].value_counts()