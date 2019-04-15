# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:25:04 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("deliveryfleet.csv")
features=dataset.iloc[:,[1,2]].values
plt.scatter(features[:,0],features[:,1])
plt.show()
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title("elbow algo.")
plt.xlabel("distance_features")
plt.ylabel("spending_features")
plt.show()
kmeans=KMeans(n_clusters=2,init="k-means++",random_state=0)
kmeans.fit(features)
pred_cluster=kmeans.fit_predict(features)
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="blue",label="cluster1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="red",label="cluster2")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title("deliveryfleet")
plt.xlabel("distance_features")
plt.ylabel("spending_features")
plt.legend()
plt.show()

-------------------------------------------------------------------------------
#for 4 block
kmeans=KMeans(n_clusters=4,init="k-means++",random_state=0)
kmeans.fit(features)
pred_cluster=kmeans.fit_predict(features)
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="blue",label="cluster1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="red",label="cluster2")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="yellow",label="cluster3")
plt.scatter(features[pred_cluster==3,0],features[pred_cluster==3,1],color="green",label="cluster4")

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'black', label = 'Centroids')
plt.title("deliveryfleet")
plt.xlabel("distance_features")
plt.ylabel("spending_features")
plt.legend()
plt.show()














