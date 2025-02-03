import pandas as pd
import re

def classify_strain(row):
    name = row['name'].lower() if isinstance(row['name'], str) else ""
    description = row['descriptionPlain'].lower() if isinstance(row['descriptionPlain'], str) else ""

    # Regular expressions for Auto and Photoperiod keywords
    auto_keywords = r"\b(auto|autoflowering|autoflower|automatic)\b"
    photoperiod_keywords = r"\b(photoperiod|light cycle|indoor|outdoor|flowering)\b"

    # Count keyword matches using regex
    auto_count = len(re.findall(auto_keywords, name)) + len(re.findall(auto_keywords, description))
    photoperiod_count = len(re.findall(photoperiod_keywords, name)) + len(re.findall(photoperiod_keywords, description))

    # Assigning higher weight for "Auto" and "Photoperiod" keywords
    auto_weight = auto_count * 2  # Increase the weight of auto-related keywords
    photoperiod_weight = photoperiod_count * 1  # Normal weight for photoperiod-related keywords

    # Apply the logic: Favour "Auto" more
    if auto_weight > photoperiod_weight:
        return 'Auto'
    elif photoperiod_weight > auto_weight:
        return 'Photoperiod'
    else:
        # In case of a tie, check if the strain mentions "auto" more prominently
        if auto_count > photoperiod_count:
            return 'Auto'
        return 'Hybrid'

# Load your CSV
df = pd.read_csv('strains_data_app_v2.csv')

# Apply the updated classification logic
df['photoperiod'] = df.apply(classify_strain, axis=1)

# Save the updated CSV
df.to_csv('strains_data_app_v3.csv', index=False)

# Check the updated distribution
photoperiod_distribution = df['photoperiod'].value_counts()

print("\nUpdated Distribution of 'photoperiod' categories:")
print(photoperiod_distribution)
