import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("results.csv")

print("\nInput Data\n")
print(data.head())

X = data[["warnings","overflow","conversion"]]

kmeans = KMeans(n_clusters=4, random_state=0)

data["cluster"] = kmeans.fit_predict(X)

data.to_csv("clustered_results.csv", index=False)

print("\nClustered Results\n")
print(data.head())

summary = data.groupby("cluster")[["warnings","overflow","conversion"]].mean()

summary.to_csv("cluster_summary.csv")

print("\nCluster Summary\n")
print(summary)

plt.scatter(data["warnings"], data["overflow"], c=data["cluster"])
plt.xlabel("warnings")
plt.ylabel("overflow")
plt.title("Clusters")
plt.savefig("clusters.png")

print("clusters.png created")
