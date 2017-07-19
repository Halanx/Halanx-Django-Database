import numpy as np
from sklearn.cluster import KMeans


def cluster_by_location(locations, lookup):
	kmeans = KMeans(n_clusters=max(1,len(locations)/4), random_state=0).fit(locations)
	labels = kmeans.predict(locations)
	clusters = []
	for x in range(len(kmeans.cluster_centers_)):
		clusters.append({'c': kmeans.cluster_centers_[x],'ids':lookup[np.where(labels==x)]})
	return clusters


def distance(a,b):
	return (a[0]-b[0])**2 + (a[1]-b[1])**2