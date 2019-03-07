# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:59:36 2019

@author: lenovo
"""

import pandas as pd
df=pd.read_csv("automobile.csv")
print(df["price"].min())
print(df["price"].max())
print(df["price"].mean())
print(df["price"].std())
print(df["price"].values)