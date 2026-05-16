#!/bin/bash

echo "=== Step 1: Update system ==="
sudo apt update

echo "=== Step 2: Install required system tools ==="
sudo apt install -y python3-pip libreoffice

echo "=== Step 3: Install Python libraries ==="
pip install pandas scikit-learn matplotlib

echo "=== Step 4: Check project folder ==="
pwd
ls

echo "=== Step 5: Show dataset preview ==="
head clustered_results.csv

echo "=== Step 6: Run clustering analysis ==="
python3 << 'EOF'
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("Loading dataset...")
df = pd.read_csv("clustered_results.csv")

# Remove cluster column if already exists
if "cluster" in df.columns:
    df = df.drop(columns=["cluster"])

features = df.drop(columns=["program"], errors="ignore")

scaler = StandardScaler()
scaled = scaler.fit_transform(features)

model = KMeans(n_clusters=3, random_state=42)
clusters = model.fit_predict(scaled)

df["cluster"] = clusters

df.to_csv("clustered_results_updated.csv", index=False)

print("Clustering complete")
print(df.head())
EOF

echo "=== Step 7: Generate cluster summary ==="
python3 << 'EOF'
import pandas as pd

df = pd.read_csv("clustered_results_updated.csv")
summary = df.groupby("cluster").size()

print("\nCluster Summary:")
print(summary)

summary.to_csv("cluster_summary.csv")
EOF

echo "=== Step 8: Create cluster plot ==="
python3 << 'EOF'
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clustered_results_updated.csv")

plt.scatter(df.iloc[:,1], df.iloc[:,2], c=df["cluster"])
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Cluster Visualization")
plt.savefig("clusters.png")
print("Cluster image saved as clusters.png")
EOF

echo "=== Step 9: Open results in LibreOffice ==="
libreoffice clustered_results_updated.csv &

echo "=== Step 10: Project finished ==="
ls
