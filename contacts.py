from utils import save_contacts_to_file

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if not name.isalpha():
        print("Error: Name must only contain letters.")
        return
    phone = input("Enter Phone Number: ").strip()
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    if phone in [contact['phone'] for contact in contacts]:
        print("Error: Duplicate phone number is not allowed.")
        return
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts_to_file(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")

def search_contacts(contacts):
    query = input("Enter search query (name, phone, email, address): ").strip().lower()
    results = [contact for contact in contacts if query in contact.values()]
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    else:
        print("No contacts match your search.")

def remove_contact(contacts):
    phone = input("Enter the phone number of the contact to remove: ").strip()
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts_to_file(contacts)
            print("Contact removed successfully!")
            return
    print("Error: Contact not found.")