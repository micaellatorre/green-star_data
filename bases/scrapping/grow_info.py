import pandas as pd
import json

# Load the curated CSV file
curated_csv_file = 'curated_strains_data.csv'
df = pd.read_csv(curated_csv_file)

# Select the specified columns
selected_columns = ['id', 'slug', 'name', 'category', 'phenotype', 'growInfo']
selected_df = df[selected_columns]

# Function to convert JSON string to dictionary
def json_to_dict(json_str):
    try:
        return json.loads(json_str.replace("'", '"'))
    except json.JSONDecodeError:
        return {}

# Apply the function to the growInfo column
grow_info_dicts = selected_df['growInfo'].apply(json_to_dict)

# Create a DataFrame from the growInfo dictionaries
grow_info_df = pd.json_normalize(grow_info_dicts)

# Concatenate the original DataFrame with the growInfo DataFrame
final_df = pd.concat([selected_df.drop(columns=['growInfo']), grow_info_df], axis=1)

# Save the final DataFrame to a new CSV file
final_df.to_csv('grow_info.csv', index=False)

# Display the first 10 rows of the final DataFrame
print(final_df.head(10))

