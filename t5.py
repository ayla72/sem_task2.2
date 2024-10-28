import scanpy as sc
import pandas as pd


# Load the dataset
adata = sc.read_h5ad("Al.h5ad")


# Extract numeric ages from the 'development_stage' column
adata.obs['age'] = adata.obs['development_stage'].str.extract(r'(\d+)', expand=False).astype(float)

# Filter for subjects aged 57 to 89
adata_age = adata[(adata.obs['age'] >= 57) & (adata.obs['age'] <= 89)].copy()

# Group by age and compute summary statistics for each age group
age_groups = adata_age.obs.groupby('age').describe()

# Export the age group statistics to a CSV file
age_groups.to_csv("age_group_statistics_57_to_89.csv")
print("Summary statistics for age groups 57 to 89 have been saved to age_group_statistics_57_to_89.csv.")
