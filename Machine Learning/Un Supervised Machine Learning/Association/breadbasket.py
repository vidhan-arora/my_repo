# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:01:45 2019

@author: lenovo
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise 
transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.








from apyori import apriori
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv('BreadBasket_DMS.csv')

dataset = dataset.replace("NONE",np.nan).dropna()

counts = dataset["Item"].value_counts()[:15]
names = list(counts.index)

plt.pie(list(counts),labels=names,autopct="%1.1f%%",radius=1.5)

plt.show()

def cart(items):
    return list(set(items))

transactions = list(dataset.groupby("Transaction")["Item"].apply(cart))

rules = list(apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3))
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