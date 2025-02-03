import pandas as pd

# Load the dataset
csv_file = 'strains_data_v0.csv'  # Replace with your file path if needed
df = pd.read_csv(csv_file)

# Define a function that assigns 'Hybrid' based on lineage logic
def assign_hybrid_based_on_lineage(row):
    if pd.isna(row['phenotype']):
        lineage = str(row.get('parents', '')).lower()
        # Define commonly dominant strains for Indica and Sativa
        dominant_strains = ['indica', 'sativa']
        
        # Check if both 'Indica' and 'Sativa' appear in the lineage
        if all(strain in lineage for strain in dominant_strains):
            return 'Hybrid'
        
        # Add additional logic here if needed based on the lineage
        # For example, checking for more specific strains could be added here.
    
    return row['phenotype']

# Apply the function to fill missing 'phenotype' values
df['phenotype'] = df.apply(assign_hybrid_based_on_lineage, axis=1)

# Final fallback: Assign 'Hybrid' for any remaining missing values
df['phenotype'] = df['phenotype'].fillna('Hybrid')

# Define the strain to test
strain_to_test = 'wubba-punch'  # Replace with the actual strain name or identifier

# Check if the strain exists in the dataset
strain_info = df[df['slug'] == strain_to_test]  # Replace 'strain_name' with the column that identifies strains
if not strain_info.empty:
    # Extract relevant details for the strain
    category = strain_info.iloc[0]['category']
    flavors = strain_info.iloc[0]['flavors']

    print(f"Testing for strain: {strain_to_test}")
    print(f"Category: {category}")
    print(f"Flavors: {flavors}")

    # Inspect the mode for the group ('category' and 'flavors')
    group_mode = df[(df['category'] == category) & (df['flavors'] == flavors)]['phenotype'].mode()

    # Print the group's mode value
    if not group_mode.empty:
        print(f"Mode phenotype for group (category: {category}, flavors: {flavors}): {group_mode[0]}")
    else:
        print(f"No mode found for group (category: {category}, flavors: {flavors}). Fallback will be applied.")

    # Apply the imputation logic with fallback to 'Hybrid' if no mode is found
    df['phenotype'] = df['phenotype'].fillna(
        df.groupby(['category', 'flavors'])['phenotype'].transform(
            lambda x: x.mode()[0] if not x.mode().empty else 'Hybrid'
        )
    )

    # Extract the imputed value for the strain
    phenotype_after = df[df['slug'] == strain_to_test]['phenotype'].iloc[0]
    print(f"Imputed phenotype for strain {strain_to_test}: {phenotype_after}")

else:
    print(f"No data found for strain: {strain_to_test}")

# Check the rows where 'phenotype' is still missing (optional)
missing_rows = df[df['phenotype'].isna()]
print("\nRows with missing phenotype after imputation:")
print(missing_rows)
