import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Halanx.settings")
django.setup()
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from Carts.models import CartItem
from ShopperBase.models import Shopper


def cluster_by_location(locations, lookup):
	kmeans = KMeans(n_clusters=2, random_state=0).fit(locations)
	labels = kmeans.predict(locations)
	batches = []
	for x in range(len(kmeans.cluster_centers_)):
		batches.append({'c': kmeans.cluster_centers_[x],'ids':lookup[np.where(labels==x)]})
	return batches



# write in view
def distance(a,b):
	return (a[0]-b[0])**2 + (a[1]-b[1])**2

# write in view
def find_shopper(centroid):
	shoppers = Shopper.objects.filter(IsOnline=True,Verified=True)
	sloc = [(s.id,distance(centroid, (s.Latitude, s.Longitude))) for s in shoppers]
	sloc = sorted(sloc, key = lambda x:x[1])
	return sloc


items = CartItem.objects.filter(RemovedFromCart=True, IsOrdered=True)
locations = np.array([(item.Item.RelatedStore.Latitude, item.Item.RelatedStore.Longitude) for item in items])
lookup = np.array([item.id for item in items])
clusters = cluster_by_location(locations, lookup)


for cluster in clusters:
	shoppers = find_shopper(cluster['c'])
