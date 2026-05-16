import pandas as pd

data = pd.read_csv("clustered_results.csv")
summary = pd.read_csv("cluster_summary.csv")

with pd.ExcelWriter("analysis.xlsx") as writer:
    data.to_excel(writer, sheet_name="data", index=False)
    summary.to_excel(writer, sheet_name="clusters", index=False)

print("Excel report created: analysis.xlsx")
