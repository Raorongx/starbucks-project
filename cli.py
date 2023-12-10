from tree import build_tree
def display_menu():
    print("Welcome to the Starbucks Store Locator")
    print("1. Search by City")
    print("2. Search by Zip Code")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print("Thank you for using the Starbucks Store Locator.")
            break
        else:
            print("Invalid choice. Please try again.")
def search_by_city(tree):
    city = input("Enter city name: ")
    # Add logic to search the tree based on city and display results

def search_by_zip(tree):
    zip_code = input("Enter zip code: ")
    # Add logic to search the tree based on zip code and display results

def main():
    tree = build_tree(load_data_from_cache())
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            search_by_city(tree)
        elif choice == '2':
            search_by_zip(tree)
        elif choice == '3':
            print("Thank you for using the Starbucks Store Locator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
