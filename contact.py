contacts = []

def add_contact(name, phone, email="", address=""):
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['Name']}, {contact['Phone']}")
    else:
        print("No contacts available.")

def search_contact(query):
    results = []
    for contact in contacts:
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            results.append(contact)
    return results

def update_contact(query, name, phone, email="", address=""):
    for i, contact in enumerate(contacts):
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            contacts[i] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(query):
    for i, contact in enumerate(contacts):
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            del contacts[i]
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def display_menu():
    print("\n===== Contact Manager =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def run_contact_manager():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email (optional): ")
            address = input("Enter Address (optional): ")
            add_contact(name, phone, email, address)

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = search_contact(query)
            if results:
                for i, contact in enumerate(results, start=1):
                    print(f"{i}. {contact['Name']}, {contact['Phone']}")
            else:
                print("No matching contacts.")

        elif choice == "4":
            query = input("Enter name or phone number to update: ")
            name = input("Enter new Name: ")
            phone = input("Enter new Phone: ")
            email = input("Enter new Email (optional): ")
            address = input("Enter new Address (optional): ")
            update_contact(query, name, phone, email, address)

        elif choice == "5":
            query = input("Enter name or phone number to delete: ")
            delete_contact(query)

        elif choice == "6":
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run_contact_manager()


