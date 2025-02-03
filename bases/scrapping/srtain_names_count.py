import json

# Load the JSON file and count the instances in "strain_names"
def count_strain_names(json_file):
    try:
        # Open and load the JSON file
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Check if "strain_names" exists and is a list
        if "strain_names" in data and isinstance(data["strain_names"], list):
            count = len(data["strain_names"])
            print(f'The "strain_names" array contains {count} instances.')
        else:
            print('"strain_names" is either missing or not a list in the JSON file.')
    
    except FileNotFoundError:
        print(f'The file {json_file} was not found.')
    except json.JSONDecodeError:
        print(f'The file {json_file} is not a valid JSON file.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Specify the JSON file
json_file = 'strain_names.json'

# Call the function
count_strain_names(json_file)
