import csv

def save_contacts_to_file(contacts):
    with open("contacts_data.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
        writer.writeheader()
        writer.writerows(contacts)

def load_contacts_from_file():
    try:
        with open("contacts_data.csv", mode="r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []