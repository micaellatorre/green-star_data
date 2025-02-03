import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url_strain = 'https://www.dummypage.com/strains/blue-dream'

# Send a GET request to the URL
response = requests.get(url_strain)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Print the HTML content (for debugging)
    print(soup.prettify())
    
    # Example: Find specific data on the page
    # For instance, getting the strain name and description
    strain_name = soup.find('h1', {'data-testid': 'strain-name'}).text.strip()
    description = soup.find('div', {'data-testid': 'strain-description'}).text.strip()
    
    # Print the results
    print(f"Strain Name: {strain_name}")
    print(f"Description: {description}")
    
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
