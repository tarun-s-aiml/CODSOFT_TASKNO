# CODSOFT Python Programming Internship
# Task 5: Contact Book

contacts = {}


def add_contact():
    name = input("\nEnter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\n========== CONTACTS ==========")

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])


def search_contact():
    name = input("\nEnter contact name to search: ").strip()

    if name in contacts:
        print("\nContact Found!")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def update_contact():
    name = input("\nEnter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    print("Contact updated successfully!")


def delete_contact():
    name = input("\nEnter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\n==============================")
        print("         CONTACT BOOK")
        print("==============================")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Contact Book closed.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
