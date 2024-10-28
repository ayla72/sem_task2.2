import scanpy as sc
import pandas as pd

# Load the dataset
adata = sc.read_h5ad("Al.h5ad")

# Check the unique values in the 'sex' column to confirm labels
print("Unique values in 'sex':", adata.obs['sex'].unique())

# Separate the data by gender
male_data = adata.obs[adata.obs['sex'] == "male"].copy()
female_data = adata.obs[adata.obs['sex'] == "female"].copy()

# Reset index for each group to clean up the dataframes
male_data.reset_index(inplace=True, drop=True)
female_data.reset_index(inplace=True, drop=True)

# Perform comparison of summary statistics between male and female cohorts
comparison_gender = male_data.describe().compare(female_data.describe())

# Rename columns to 'Male' and 'Female' instead of 'self' and 'other' for clarity
comparison_gender.columns = comparison_gender.columns.map(lambda x: ('Male' if x[0] == 'self' else 'Female', x[1]))

# Display the comparison result
print("Comparison of summary statistics between male and female cohorts:")
print(comparison_gender)

comparison_gender.to_csv("gender_cohort_comparison.csv")
