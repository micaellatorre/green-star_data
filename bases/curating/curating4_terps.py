import pandas as pd
import json
from collections import Counter

# Load the CSV file
csv_file = 'strains_data_v2.csv'
df = pd.read_csv(csv_file)

# Convert '{}' to None for proper handling
df['terps'] = df['terps'].apply(lambda x: None if x == '{}' else x)

# Step 1: Extract prefixes and suffixes from 'slug'
def get_prefix_suffix(slug):
    if isinstance(slug, str):
        parts = slug.split('-')
        return parts[0], parts[-1]
    return None, None

df[['prefix', 'suffix']] = df['slug'].apply(lambda x: pd.Series(get_prefix_suffix(x)))

# Step 2: Identify unique prefix-suffix combinations
df['prefix_suffix_group'] = df['prefix'] + '-' + df['suffix']

# Step 3: Count the occurrences of each prefix-suffix group
prefix_suffix_counts = df['prefix_suffix_group'].value_counts()

print("\nMost common prefix-suffix groups:")
print(prefix_suffix_counts.head(10))

# Step 4: Calculate mode of 'terps' for each group
group_modes = {}

for group in df['prefix_suffix_group'].dropna().unique():
    group_data = df[(df['prefix_suffix_group'] == group) & df['terps'].notna()]['terps']
    if not group_data.empty:
        group_modes[group] = group_data.mode()[0]

print("\nMode of 'terps' by prefix-suffix group:")
print({k: v for k, v in list(group_modes.items())[:10]})  # Print first 10 group modes

# Step 5: Fill missing 'terps' using prefix-suffix group modes
def fill_terps_from_group(row):
    if pd.isna(row['terps']) and row['prefix_suffix_group'] in group_modes:
        return group_modes[row['prefix_suffix_group']]
    return row['terps']

df['terps'] = df.apply(fill_terps_from_group, axis=1)

# Step 6: Final fallback to fill remaining missing 'terps' with overall mode
terps_non_empty = df.dropna(subset=['terps'])['terps']
overall_mode = terps_non_empty.mode().iloc[0] if not terps_non_empty.empty else None
df['terps'] = df['terps'].fillna(overall_mode)

# Verify if any missing data remains in 'terps'
missing_terps_after = df['terps'].isna().sum()
print(f"\nMissing 'terps' values after completion: {missing_terps_after}")

# Save the updated DataFrame to a new CSV
output_file = 'strains_data_v2_completed2.csv'
df.to_csv(output_file, index=False)

print(f"\nUpdated data saved to {output_file}")
