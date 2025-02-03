import pandas as pd
import ast

# Load the CSV file
csv_file = 'strains_data_v4.csv'
df = pd.read_csv(csv_file)

# Step 1: Convert 'growInfo' from string to dictionary (if necessary)
df['growInfo'] = df['growInfo'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Step 2: Check for missing values (None) for key-value pairs in the 'growInfo' column
missing_values_summary = df['growInfo'].apply(lambda x: {k: v is None for k, v in x.items()}).apply(pd.Series).sum()
print("Missing Values Summary:")
print(missing_values_summary)

# Step 3: Handle missing values by filling with the most frequent value for each key
# Identify common values for the keys where we expect the most frequent value
common_values = {}

# Calculate the mode for each key (column)
for key in missing_values_summary.index:
    if key not in ['growNotes', 'growNotesPlain']:  # Skip textual fields like 'growNotes'
        common_values[key] = df['growInfo'].apply(lambda x: x.get(key) if x.get(key) is not None else None).mode().iloc[0]

# Step 4: Fill missing values based on the common values
def fill_missing_values(growinfo):
    for key, value in common_values.items():
        if growinfo.get(key) is None:
            growinfo[key] = value
    return growinfo

# Apply the filling function to the 'growInfo' column
df['growInfo'] = df['growInfo'].apply(fill_missing_values)

# Step 5: Save the updated DataFrame to a new CSV file
output_file = 'strains_data_v5.csv'
df.to_csv(output_file, index=False)

print(f"\nUpdated data saved to {output_file}")
