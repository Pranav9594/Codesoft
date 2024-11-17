class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    # Add contact 
    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully.")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone}")

    # Search for contact by name or phone number
    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == search_term.lower() or contact.phone == search_term]
        if not found_contacts:
            print(f"No contacts found for '{search_term}'.")
        else:
            for contact in found_contacts:
                self.display_contact(contact)

    # Update contact details
    def update_contact(self, search_term):
        for contact in self.contacts:
            if contact.name.lower() == search_term.lower() or contact.phone == search_term:
                print("Contact found. Enter new details:")
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print(f"Contact {contact.name} updated successfully.")
                return
        print(f"No contacts found for '{search_term}'.")

    # Delete contact by name or phone number
    def delete_contact(self, search_term):
        for contact in self.contacts:
            if contact.name.lower() == search_term.lower() or contact.phone == search_term:
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully.")
                return
        print(f"No contacts found for '{search_term}'.")

    # Display full contact details
    def display_contact(self, contact):
        print(f"\nName: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

def user_interface():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting contact book. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    user_interface()
