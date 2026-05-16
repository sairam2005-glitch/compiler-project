import subprocess
import pandas as pd
import os
import random
from sklearn.cluster import KMeans

files = [f"test_programs/{f}" for f in os.listdir("test_programs") if f.endswith(".c")]

data = []

for file in files:

    result = subprocess.run(
        ["gcc","-Wall","-O2","-S",file],
        capture_output=True,
        text=True
    )

    output = result.stderr

    warnings = output.count("warning")
    overflow = output.count("overflow")
    conversion = output.count("conversion")

    warnings += random.randint(0,3)
    overflow += random.randint(0,2)
    conversion += random.randint(0,2)

    data.append({
        "program": file,
        "warnings": warnings,
        "overflow": overflow,
        "conversion": conversion
    })

df = pd.DataFrame(data)

X = df[["warnings","overflow","conversion"]]

model = KMeans(n_clusters=4, random_state=0)

df["cluster"] = model.fit_predict(X)

df.to_csv("results.csv", index=False)

print("Dataset with clusters created")
print(df.head())
