# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

# data = pd.read_csv("data.csv")

# kmeans = KMeans(n_clusters=2, init=[[2, 1], [2, 3]], n_init=1)
# kmeans.fit(data)
# data["cluster"] = kmeans.labels_
# print("Data with assigned clusters:\n", data)
# print("\nCluster centers:\n", kmeans.cluster_centers_)

# plt.scatter(data["x1"], data["x2"], c=kmeans.labels_, cmap="viridis", s=100, label="Data points")
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],c="red", marker="X", s=200, label="Cluster centres")
# plt.xlabel("x1")
# plt.ylabel("x2")
# plt.title("K-Means Clustering (k=2)")
# plt.legend()
# plt.savefig("kmeans_plot.png")
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("data.csv")

model = KMeans(n_clusters=2, init=[[2,1], [2,3]], n_init=1)
model.fit(data)
data["cluster"] = model.labels_
centroids = model.cluster_centers_
print("The assigned cluster are : \n", data)
print("The center points : \n", centroids)

plt.figure(figsize=(8,6))
plt.scatter(data["x1"], data["x2"], c=model.labels_, cmap="viridis", s=200, label="Points")
plt.scatter(centroids[:,0], centroids[:,1], c="red", marker="x", s=100, label="Cluster center")
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Kmeans algo")
plt.grid(True)
plt.legend()
plt.show()
