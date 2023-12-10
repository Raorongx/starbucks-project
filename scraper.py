import requests
from bs4 import BeautifulSoup
import json

def scrape_starbucks_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stores = soup.find_all('div', class_='store')
    store_data = []

    for store in stores:
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


url = 'https://www.starbucks.com/store-locator'
data = scrape_starbucks_data(url)


with open('cache.json', 'w') as file:
    json.dump(data, file)

def save_data_to_cache(data):
    with open('cache.json', 'w') as file:
        json.dump(data, file)

def main():
    try:
        data = scrape_starbucks_data(url)
        if data:
            save_data_to_cache(data)
            print(f"Successfully scraped {len(data)} records.")
        else:
            print("No data was scraped.")
    except Exception as e:
        print(f"Error occurred during scraping: {e}")

if __name__ == "__main__":
    main()
