import scanpy as sc


# Load the dataset
adata = sc.read_h5ad("Al.h5ad")


# Split into subjects (optional, if you need individual subject data)
subjects = {}
subject_ids = adata.obs['donor_id'].unique()

# Split into normal and Alzheimer disease groups
normal = adata.obs.loc[adata.obs['disease'] == "normal"].copy()
ad = adata.obs.loc[adata.obs['disease'] == "Alzheimer disease"].copy()

# Reset index for each group
normal.reset_index(inplace=True, drop=True)
ad.reset_index(inplace=True, drop=True)

# Perform comparison of summary statistics between normal and Alzheimer groups
comparison = normal.describe().compare(ad.describe())
print("Comparison of summary statistics between normal and Alzheimer disease groups:")
print(comparison)
comparison.to_csv("Al_vs_normal.csv")
