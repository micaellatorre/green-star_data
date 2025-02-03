import pandas as pd
import numpy as np

# Load the dataset
csv_file = 'strains_data_v5.csv'  # Adjust the filename if necessary
df = pd.read_csv(csv_file)

# Check for missing values in descriptionPlain
missing_count = df['descriptionPlain'].isna().sum()
print(f"Missing values in 'descriptionPlain': {missing_count}")

# Generate placeholder descriptions for missing cells
def generate_placeholder(row):
    """
    Generates a placeholder description based on other data in the row.
    """
    phenotype = row['phenotype'] if pd.notna(row['phenotype']) else "Hybrid"
    flavors = row['flavors'] if pd.notna(row['flavors']) else "a mix of flavors"
    effects = row['effects'] if pd.notna(row['effects']) else "varied effects"
    
    return f"This strain is a {phenotype} phenotype with {flavors} and provides {effects}."

# Apply the placeholder generation to missing descriptionPlain cells
df['descriptionPlain'] = df.apply(
    lambda row: generate_placeholder(row) if pd.isna(row['descriptionPlain']) else row['descriptionPlain'],
    axis=1
)

# Verify that there are no more missing values
missing_count_after = df['descriptionPlain'].isna().sum()
print(f"Missing values after curation: {missing_count_after}")

# Save the curated dataset
output_file = 'strains_data_v6.csv'
df.to_csv(output_file, index=False)
print(f"Curated dataset saved to {output_file}")