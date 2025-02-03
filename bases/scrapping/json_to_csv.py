import json
import pandas as pd

# Load the JSON file with strain data
with open('strains_data.json', 'r') as f:
    strains_data = json.load(f)['strains_data']

# Define the columns we want to extract
columns = [
    'slug', 'id', 'averageRating', 'award', 'cannabinoids', 'category',
    'celebrationColors', 'children', 'conditionReviewCount', 'conditions',
    'description', 'descriptionPlain', 'effectReviewCount', 'effects',
    'energizeScore', 'flavorReviewCount', 'flavors', 'flowerImagePng',
    'flowerImageSvg', 'growInfo', 'highlightedPhotos', 'name',
    'negativeReviewCount', 'negatives', 'nucleusImagePng', 'nucleusImageSvg',
    'nugImage', 'nugImageAltText', 'parents', 'phenotype', 'photoCount',
    'rating', 'reviewCount', 'stockNugImage', 'subtitle', 'symbol',
    'symptomReviewCount', 'symptoms', 'terps', 'topEffect', 'totalFollowers',
    'traitsCountTotal', 'traitsSourceCountTotal'
]

# Create a list of dictionaries with the required columns
data = []
for strain in strains_data:
    row = {}
    for col in columns:
        row[col] = strain.get(col)
    data.append(row)

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('strains_data.csv', index=False)

print("Data has been successfully converted to strains_data.csv")
