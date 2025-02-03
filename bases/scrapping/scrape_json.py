import requests
import json

# Load the JSON file with strain names
with open('strain_names.json', 'r') as f:
    strain_names_data = json.load(f)

# Get URL for the strain from .enviroment variable
base_url_scrape = "https://www.dummypage.com/_next/data/{key}/strains/{}.json?strainSlug={}"

# List to hold the strain data
strains_data = []

# Iterate over each strain name
for strain in strain_names_data['strain_names']:
    slug = strain['slug']
    url = base_url_scrape.format(slug, slug)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Access the nested dictionary
        try:
            strain_data = data['pageProps']['strain']
            strains_data.append(strain_data)
            print(f"Successfully retrieved data for slug: {slug}")
        except KeyError as e:
            print(
                f"KeyError: {e} not found in the JSON response for slug: {slug}"
            )
    else:
        print(
            f"Failed to retrieve data for slug: {slug}. HTTP Status code: {response.status_code}"
        )

# Save the strain data to a JSON file
with open('strains_data.json', 'w') as f:
    json.dump({'strains_data': strains_data}, f, indent=4)

print("Scraping completed and data saved to strains_data.json")
