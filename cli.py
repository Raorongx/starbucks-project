import json
from tree import TreeNode, build_tree
import webbrowser
import requests

def load_data_from_cache():
    with open('starbucks_locations.json', 'r') as file:
        return json.load(file)

def display_menu(name="Welcome to the Starbucks Store Locator"):
    print(name)
    print("1. Search by City")
    print("2. Search by Zip Code")
    print("3. View in Google Maps")
    print("4. View All Stores")
    print("5. Exit")

def search_by_city(root, city_name):
    city_name = city_name.lower().strip()
    found = False
    for city_node in root.children:
        if city_name in city_node.name.lower() or city_node.name.lower() in city_name:
            print(f"Stores in {city_node.name}:")
            for store_node in city_node.children:
                print(f"- {store_node.name}")
            found = True
            break
    if not found:
        print(f"No stores found in {city_name}.")

def get_city_from_zip_code(zip_code):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zip_code}&key=AIzaSyCdF542m7ROv0k0xvgUA7UnDMn3EY9x0oE"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        for component in data['results'][0]['address_components']:
            if 'locality' in component['types']:
                return component['long_name']
    return None

def search_by_zip(root, zip_code):
    zip_code = zip_code.strip()
    found = False
    print(f"Stores in zip code {zip_code}:")
    city_name = get_city_from_zip_code(zip_code)
    for city_node in root.children:
        city_has_zip_code = False
        for store_node in city_node.children:
            store_zip = getattr(store_node, 'zip_code', 'Unknown')

            if store_zip == zip_code or (store_zip == 'Unknown' and city_node.name == city_name):
                print(f"- {store_node.name} (City: {city_node.name})")
                found = True
                city_has_zip_code = True

        if city_has_zip_code and not found:
            # If the city matches the zip code but no stores have a known zip code
            for store_node in city_node.children:
                print(f"- {store_node.name} (City: {city_node.name}, Zip: Unknown)")
                found = True

    if not found:
        print("No stores found.")



def view_in_real():
    city_name = input("Enter city name to view Starbucks stores on Google Maps: ")
    search_query = f"Starbucks in {city_name}"
    search_query_encoded = search_query.replace(" ", "+")
    url = f"https://www.google.com/maps/search/{search_query_encoded}"
    webbrowser.open(url)
    print(f"Opening Google Maps for Starbucks stores in {city_name}.")

def view_all_stores(root):
    print("All Starbucks Stores:")
    for city_node in root.children:  # Iterate over city nodes
        print(f"City: {city_node.name}")
        for store_node in city_node.children:  # Iterate over store nodes within each city
            print(f"  - {store_node.name}")

def main():
    data = load_data_from_cache()
    tree = build_tree(data)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter city name: ")
            search_by_city(tree, city)
        elif choice == '2':
            zip_code = input("Enter zip code: ")
            search_by_zip(tree, zip_code)
        elif choice == '3':
            view_in_real()
        elif choice == '4':
            view_all_stores(tree)
        elif choice == '5':
            print("Thank you for using the Starbucks Store Locator.")
            break
        else:
            print("Invalid choice. Please try again.")
                        
        print("\n\n")

if __name__ == "__main__":
    main()