import scanpy as sc

# Define the specific genes based on your provided list
genes_of_interest = [
    "SLC26A3", "RASGEF1B", "RP11-701H24.9", "LINGO1", "PDE4DIP",
    "AC159540.1", "RP11-289H16.1", "RP11-219A15.1", "LINC01609",
    "PHYHIP", "RP11-745L13.2"
]

# Load your dataset into an AnnData object
adata = sc.read_h5ad("Al.h5ad")

# Inspect the first few rows of adata.var to understand how gene names are stored
print(adata.var.head())

# Use the identified column (e.g., 'feature_name') to filter genes
if 'feature_name' in adata.var.columns:
    adata_filtered = adata[:, adata.var['feature_name'].isin(genes_of_interest)].copy()
else:
    # Fallback if names are directly in var_names
    adata_filtered = adata[:, [gene for gene in genes_of_interest if gene in adata.var_names]].copy()

# Check the filtered dataset to confirm genes are loaded
print(adata_filtered)



