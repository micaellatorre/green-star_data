import requests
from bs4 import BeautifulSoup
import json

base_url_strain = "https://www.dummypage.com/strains?sort=strain_name%3Aasc&page={}"
total_pages = 454  # Change this to the actual number of pages
strain_names = []

def get_strain_names_from_page(page_number):
    url = base_url_strain.format(page_number)
    response = requests.get(url)
    print(f"Fetching URL: {url}")
    if response.status_code == 200:
        print(f"Successfully fetched page {page_number}")
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.find('script', {'id': '__NEXT_DATA__'})
        if script_tag:
            script_content = script_tag.string
            data = json.loads(script_content)
            strains = data['props']['pageProps']['data']['strains']
            for strain in strains:
                strain_id = strain['id']
                strain_slug = strain['slug']
                print(f"Found strain: id={strain_id}, slug={strain_slug}")
                strain_names.append({'id': strain_id, 'slug': strain_slug})
        else:
            print("Failed to find __NEXT_DATA__ script tag")
    else:
        print(f"Failed to retrieve data from page {page_number}. Status code: {response.status_code}")

# Iterate through all pages and scrape strain names
for page_number in range(1, total_pages + 1):
    print(f"Scraping page {page_number}...")
    get_strain_names_from_page(page_number)

# Save the strain names to a JSON file
with open('strain_names.json', 'w') as f:
    json.dump({'strain_names': strain_names}, f, indent=4)

print("Scraping completed and data saved to strain_names.json")
