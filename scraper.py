import requests
from bs4 import BeautifulSoup
import json

def scrape_starbucks_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Assuming each store is in a div with a class 'store'
    stores = soup.find_all('div', class_='store')
    store_data = []

    for store in stores:
        # Extract store details like name, location, city, zip code
        # This depends on the HTML structure of the webpage
        name = store.find('h2').text
        location = store.find('p', class_='location').text
        city = store.find('span', class_='city').text
        zip_code = store.find('span', class_='zip').text

        store_data.append({
            'name': name,
            'location': location,
            'city': city,
            'zip_code': zip_code
        })

    return store_data

# Example URL (replace with the actual URL you choose)
url = 'https://www.starbucks.com/store-locator'
data = scrape_starbucks_data(url)

# Save data to JSON file
with open('cache.json', 'w') as file:
    json.dump(data, file)
