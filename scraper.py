import requests
import json
import re

def get_lat_lng(location, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}"
    res = requests.get(url)
    data = res.json()
    if data['results']:
        lat_lng = data['results'][0]['geometry']['location']
        return f"{lat_lng['lat']},{lat_lng['lng']}"
    else:
        print("The location or address is incorrect. Please try again.")
        return None

def get_places(location, radius, api_key):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    places_type = "cafe"
    keyword = "starbucks"

    request_url = f"{url}location={location}&radius={radius}&type={places_type}&keyword={keyword}&key={api_key}"
    res = requests.get(request_url)
    data = res.json()
    return data['results']

def view_all_stores(tree):
    print("All Starbucks Stores:")
    for store in tree:
        store_name = store.get('name', 'N/A')  
        city_name = store.get('plus_code', {}).get('compound_code', 'N/A').split(' ')[-1]   
        print(f"- {store_name} (City: {city_name})")

def extract_zip_code(address):
    match = re.search(r'\b\d{5}(?:-\d{4})?\b', address)
    return match.group(0) if match else 'Unknown'

def main():
    api_key = 'AIzaSyCdF542m7ROv0k0xvgUA7UnDMn3EY9x0oE'
    location_input = input("Please enter a city name or zip code: ")
    radius = input("Please enter the range(m) around the city you just entered: ")
    try:
        location = get_lat_lng(location_input, api_key) 
        if location:
            data = get_places(location, radius, api_key)
            if data:
                stores_data = []
                # print(data[1])
                for store in data:
                    city_data = store.get('plus_code', {}).get('compound_code', 'N/A').split(' ')
                    city_name = ''
                    for i in range(1, len(city_data)-1):
                        city_name += city_data[i] + ' '
                    city_name = city_name[:-2]
                    store_address = store.get('vicinity', 'N/A')
                    zip_code = extract_zip_code(store_address)  # Extract zip code from the address
                    store_info = {
                        "city": city_name,
                        "name": f"{store['name']} - {store_address}",
                        "zip_code": zip_code  # Include zip code in store info
                    }
                    stores_data.append(store_info)
        

                with open('starbucks_locations.json', 'w') as file:
                    json.dump(stores_data, file)
                print(f"Successfully retrieved {len(data)} Starbucks locations around {location_input}.")
            else:
                print("No Starbucks was found around this location. Try increasing the radius or another location.")
        else:
            print("Please provide a valid city name or zip code.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
