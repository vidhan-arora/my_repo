# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:41:33 2019

@author: lenovo
"""

Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature)
 and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from 
    those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("deliveryfleet.csv")
features=dataset.iloc[:,[1,2]].values
from sklearn.cluster import KMeans   
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title("elbow method")
plt.xlabel("cluster")
plt.ylabel("wcss")
plt.show()
kmeans=KMeans(n_clusters=2,init="k-means++",random_state=0)
pred_cluster=kmeans.fit_predict(features)
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="blue",label="cluster1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="red",label="cluster2")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="yellow",label="centroid")
plt.title("delivery fleet")
plt.xlabel("features1")
plt.ylabel("features2")
plt.legend()
plt.show()    
#for more finer way we increase the clusters.
kmeans=KMeans(n_clusters=4,init="k-means++",random_state=0)
pred_cluster=kmeans.fit_predict(features)
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],color="blue",label="cluster1")
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],color="red",label="cluster2")
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],color="green",label="cluster1")
plt.scatter(features[pred_cluster==3,0],features[pred_cluster==3,1],color="cyan",label="cluster2")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color="yellow",label="centroid")
plt.title("deliveryfleet")
plt.xlabel("features1")
plt.ylabel("fwatures2")
plt.legend()
plt.show()  


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    