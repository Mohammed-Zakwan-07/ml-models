# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.spatial.distance import pdist, squareform
# from scipy.cluster.hierarchy import linkage, dendrogram
# from sklearn.cluster import AgglomerativeClustering
 
# data = pd.read_csv("data.csv")
# dist_matrix = squareform(pdist(data, metric="euclidean"))
# print("Distance matrix:\n", pd.DataFrame(dist_matrix, index=data.index, columns=data.index), "\n")
 
# agg = AgglomerativeClustering(n_clusters=2, linkage="single")
# data["cluster"] = agg.fit_predict(data)
# print("Data with assigned clusters:\n", data)

# Z = linkage(pdist(data[["x1", "x2"]]), method="single")
 
# plt.figure()
# dendrogram(Z, labels=[f"P{i}" for i in data.index])
# plt.title("Dendrogram (Single Linkage)")
# plt.xlabel("Data points")
# plt.ylabel("Distance")
# plt.savefig("dendrogram.png")
# # plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

data = pd.DataFrame([
  {"x1":1,"x2":2},
  {"x1":2,"x2":2},
  {"x1":3,"x2":2},
  {"x1":3,"x2":3},
  {"x1":4,"x2":1},
  {"x1":4,"x2":3},
  {"x1":5,"x2":4},
  {"x1":6,"x2":3},
  {"x1":7,"x2":6},
  {"x1":7,"x2":5},
])

dist_mat = squareform(pdist(data, metric="euclidean"))
print("The distance matrix ", pd.DataFrame(dist_mat, index=data.index, columns=data.index))

model = AgglomerativeClustering(n_clusters=2, linkage="single")
model.fit(data)
data["clusters"] = model.labels_
print(data)
Z = linkage(pdist(data[["x1","x2"]]), method="single")

plt.figure(figsize=(8,6))
dendrogram(Z, labels=[f"P{i}" for i in data.index])
plt.xlabel("The points")
plt.ylabel("The something")
plt.title("Dendrogram")
plt.show()