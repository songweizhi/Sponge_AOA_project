import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# 1. Load the P/A matrix from a file
# Change 'matrix_data.csv' to your actual file name
# Use sep='\t' instead of sep=',' if your file is tab-separated
df = pd.read_csv('/Users/songweizhi/Desktop/AOA_genomes_faa_GapSeq_df.txt', index_col=0, sep='\t')

# Convert the dataframe into a raw NumPy binary array
pa_matrix = df.to_numpy()

# Extract row names for the plot labels
row_names = df.index.tolist()

# 2. Compute Jaccard distance
distance_matrix = pdist(pa_matrix, metric='jaccard')

# 3. Perform hierarchical clustering
Z = linkage(distance_matrix, method='average')

# 4. Plot the resulting dendrogram
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=row_names, leaf_rotation=90)
plt.title("Hierarchical Clustering of P/A Matrix")
plt.ylabel("Jaccard Distance")
plt.tight_layout()
plt.show()
