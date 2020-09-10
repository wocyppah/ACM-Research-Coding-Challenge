# Daniel Segundo
# 09-09-20
# Inputs: "ClusterPlot.csv" containing 150 unique clusters on individual rows
# Outputs: The number of clusters in the .csv file

# The pandas library will be used to read the file
import pandas as pd

# The file is initialized and the number of clusters is found with len()
cluster_df = pd.read_csv("C:/Users/Daniel/ACM-Research-Coding-Challenge/ClusterPlot.csv")
count = len(cluster_df)

print("Total clusters in ClustePlot.csv:", count)
