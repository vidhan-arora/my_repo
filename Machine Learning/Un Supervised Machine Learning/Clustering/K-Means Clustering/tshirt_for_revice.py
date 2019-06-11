# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:01:43 2019

@author: lenovo
"""

Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large.
 How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("tshirts.csv")
features=dataset.iloc[:,[1,2]].values
plt.scatter(features[:,0],features[:,1])
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(features)6
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel("clusters")
plt.ylabel("wcss")
plt.title("the elbow method")
plt.show()
kmeans=KMeans(n_clusters=3,init="k-means++",random_state=0)
pred_cluster=kmeans.fit_predict(features)

plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="red",label="cluster_1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="yellow",label="cluster_2")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="green",label="cluster_3")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="black",label="centroids")
plt.title("tshirts")
plt.xlabel("height")
plt.ylabel("weight")
plt.legend()
plt.show()
























