from contacts import add_contact, view_contacts, search_contacts, remove_contact
from utils import load_contacts_from_file

def main_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Remove Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    contacts = load_contacts_from_file()

    while True:
        choice = main_menu()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            remove_contact(contacts)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()