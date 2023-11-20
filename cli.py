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

if __name__ == "__main__":
    main()
