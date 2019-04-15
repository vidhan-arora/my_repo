# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:35:56 2019

@author: lenovo
"""

# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
features = dataset.iloc[:, [3, 4]].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans

"""
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
"""


# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)



# Visualizing the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'cyan', label = 'Cluster 4')
plt.scatter(features[pred_cluster == 4, 0], features[pred_cluster == 4, 1], c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature)
 and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from 
    those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.




Q1. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large.
 How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.