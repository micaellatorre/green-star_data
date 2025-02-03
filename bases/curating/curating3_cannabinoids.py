import pandas as pd

# Load the CSV file
csv_file = 'strains_data_v0.csv'
df = pd.read_csv(csv_file)

# Step 1: Count missing values ('{}') in the 'cannabinoids' column
missing_cannabinoids_count = df['cannabinoids'].apply(lambda x: x == '{}').sum()
print(f"Count of missing 'cannabinoids' values (): {missing_cannabinoids_count}")

# Step 2: Convert '{}' to None for proper handling
df['cannabinoids'] = df['cannabinoids'].apply(lambda x: None if x == '{}' else x)

# Step 3: Extract prefixes and suffixes from 'slug'
def get_prefix_suffix(slug):
    if isinstance(slug, str):
        parts = slug.split('-')
        return parts[0], parts[-1]
    return None, None

df[['prefix', 'suffix']] = df['slug'].apply(lambda x: pd.Series(get_prefix_suffix(x)))

# Step 4: Identify unique prefix-suffix combinations
df['prefix_suffix_group'] = df['prefix'] + '-' + df['suffix']

# Step 5: Count occurrences of each prefix-suffix group
prefix_suffix_counts = df['prefix_suffix_group'].value_counts()

print("\nMost common prefix-suffix groups:")
print(prefix_suffix_counts.head(10))

# Step 6: Calculate mode of 'cannabinoids' for each prefix-suffix group
group_modes_cannabinoids = {}

for group in df['prefix_suffix_group'].dropna().unique():
    group_data = df[(df['prefix_suffix_group'] == group) & df['cannabinoids'].notna()]['cannabinoids']
    if not group_data.empty:
        group_modes_cannabinoids[group] = group_data.mode()[0]

print("\nMode of 'cannabinoids' by prefix-suffix group:")
print({k: v for k, v in list(group_modes_cannabinoids.items())[:10]})  # Print first 10 group modes

# Step 7: Fill missing 'cannabinoids' using prefix-suffix group modes
def fill_cannabinoids_from_group(row):
    if pd.isna(row['cannabinoids']) and row['prefix_suffix_group'] in group_modes_cannabinoids:
        return group_modes_cannabinoids[row['prefix_suffix_group']]
    return row['cannabinoids']

df['cannabinoids'] = df.apply(fill_cannabinoids_from_group, axis=1)

# Step 8: Final fallback to fill remaining missing 'cannabinoids' with overall mode
cannabinoids_non_empty = df.dropna(subset=['cannabinoids'])['cannabinoids']
overall_mode_cannabinoids = cannabinoids_non_empty.mode().iloc[0] if not cannabinoids_non_empty.empty else None
df['cannabinoids'] = df['cannabinoids'].fillna(overall_mode_cannabinoids)

# Step 9: Verify if any missing data remains in 'cannabinoids'
missing_cannabinoids_after = df['cannabinoids'].isna().sum()
print(f"\nMissing 'cannabinoids' values after completion: {missing_cannabinoids_after}")

# Save the updated DataFrame to a new CSV
# output_file = 'strains_data_v2_completed2.csv'
# df.to_csv(output_file, index=False)

# print(f"\nUpdated data saved to {output_file}")
