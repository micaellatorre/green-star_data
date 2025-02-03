import json

# Load the JSON file
with open('strain_names.json', 'r') as f:
    data = json.load(f)

# Count the number of strain names
strain_names_count = len(data['strain_names'])

print(f"Total number of strain names: {strain_names_count}")

# Total number of strain names: 8169