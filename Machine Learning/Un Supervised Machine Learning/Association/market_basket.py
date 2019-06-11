# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 02:25:16 2019

@author: lenovo
"""

Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model,
 remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.

import pandas as pd
import numpy as np
from apyori import apriori
dataset=pd.read_csv("Market_Basket_Optimisation.csv",header=None)
def cart(item):
    if item is np.nan:
        return ""
    else:
        return item

trans = []
for var in range(0,7501):
    trans.append([str(dataset.values[var][var2]) for var2 in range(0,20) if str(dataset.values[var][var2]) != "nan" ])
    
#trans = dataset.applymap(lambda x: [x] if pd.notnull(x) else []).sum(1).tolist()


rules = apriori(trans, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
rules=list(rules)
for item in rules:

    # first index of the inner list
    # Contains base item and add item
    
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")