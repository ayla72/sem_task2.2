import scanpy as sc

# Load the dataset into an AnnData object
adata = sc.read_h5ad("Specific Dataset Cohort.h5ad")

# Check the basic structure and dimensions of the dataset
print(adata)
