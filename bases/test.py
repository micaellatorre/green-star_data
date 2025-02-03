import pandas as pd

# Load the dataset
csv_file = 'strains_data_v0.csv'  # Replace with your file path if needed
df = pd.read_csv(csv_file)

# Define the strain to test
strain_to_test = 'wonka-mints'  # Replace with the actual strain name or identifier

# Check if the strain exists in the dataset
strain_info = df[df['slug'] == strain_to_test]  # Replace 'slug' with the column that identifies strains
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

    # Apply the imputation logic to verify
    imputed_phenotype = df.groupby(['category', 'flavors'])['phenotype'].transform(
        lambda x: x.mode()[0] if not x.mode().empty else 'Hybrid'
    )

    # Update the DataFrame (simulated) and extract the imputed value for the strain
    df['phenotype'] = df['phenotype'].fillna(imputed_phenotype)
    phenotype_after = df[df['slug'] == strain_to_test]['phenotype'].iloc[0]
    print(f"Imputed phenotype for strain {strain_to_test}: {phenotype_after}")

else:
    print(f"No data found for strain: {strain_to_test}")

# Check the rows where 'phenotype' is still missing (optional)
missing_rows = df[df['phenotype'].isna()]
print("\nRows with missing phenotype after imputation:")
print(missing_rows)
