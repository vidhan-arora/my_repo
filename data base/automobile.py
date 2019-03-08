# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:59:36 2019

@author: lenovo
"""

import pandas as pd
df=pd.read_csv("automobile.csv")
print(df["price"].min()) #for minimum value
print(df["price"].max())#for maximum value
print(df["price"].mean())#for avg.
print(df["price"].std())#for standard deviation
print(df["price"].values) #for ndarray
df["price"]=df["price"].fillna(method="ffill")
