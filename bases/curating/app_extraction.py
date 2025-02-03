import pandas as pd

# Load the original CSV file
csv_file = 'strains_data_v6.csv'
df = pd.read_csv(csv_file)

# Specify the columns to keep
columns_to_keep = ['id', 'slug', 'name', 'descriptionPlain', 'phenotype', 'cannabinoids', 'terps', 'parents', 'children', 'growInfo']

# Create a new DataFrame with only the specified columns
curated_df = df[columns_to_keep]

# Save the curated DataFrame to a new CSV file
curated_csv_file = 'strains_data_app_v1.csv'
curated_df.to_csv(curated_csv_file, index=False)

print(f"Curated CSV saved to {curated_csv_file}")
