# CODSOFT Task-5: Contact Book

contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts[name.lower()] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"\nContact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("\nNo contacts found!\n")
        return
    
    print("\n--- All Contacts ---")
    for c in contacts.values():
        print(f"Name: {c['name']} | Phone: {c['phone']}")
    print(f"Total: {len(contacts)} contacts\n")

def search_contact():
    search = input("Enter Name or Phone to search: ").lower().strip()
    found = False
    for c in contacts.values():
        if search in c['name'].lower() or search in c['phone']:
            print(f"\nFound:\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n")
            found = True
    if not found:
        print("No matching contact found!\n")

def update_contact():
    name = input("Enter Name to update: ").lower().strip()
    if name not in contacts:
        print("Contact not found!\n")
        return
    
    print(f"Updating {contacts[name]['name']} (leave blank to keep same)")
    phone = input(f"New Phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"New Email [{contacts[name]['email']}]: ").strip()
    address = input(f"New Address [{contacts[name]['address']}]: ").strip()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    
    print("Contact updated!\n")

def delete_contact():
    name = input("Enter Name to delete: ").lower().strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted!\n")
    else:
        print("Contact not found!\n")

def main():
    while True:
        print("=== CODSOFT CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()