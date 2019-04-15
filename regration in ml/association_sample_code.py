# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:42:16 2019

@author: lenovo
"""
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

"""This will check each element before entering it into the list and drop the nan value"""
transactions = dataset.apply(lambda x: x.dropna().tolist(), axis=1).tolist()
#transactions=dataset.applymap(lambda x: [x] if pd.notnull(x) else []).sum(1).tolist()


rules = list(apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4))
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

