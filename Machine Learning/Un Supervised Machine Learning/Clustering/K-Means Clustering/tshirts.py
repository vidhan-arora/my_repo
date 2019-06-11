# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:06:16 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("tshirts.csv")
features=dataset.iloc[:,[1,2]].values
plt.scatter(features[:,0],features[:,1])
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title("elbow graph")
plt.xlabel("weight")
plt.ylabel("height")
plt.show()
#visulization of cluster
kmeans=KMeans(n_clusters=3,init="k-means++",random_state=0)
pred_cluster=kmeans.fit_predict(features)
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="blue",label="cluster1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="red",label="cluster2")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="black",label="cluster3")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="yellow",label="centroid")
plt.title("tshirts_size")
plt.xlabel("weight")
plt.ylabel("height")
plt.legend()
plt.show()
