import csv
import sys

# In-memory storage for contacts
# Format: {phone_number: {"name": name, "email": email}}
contacts = {}


def add_contact():
    """Adds a new contact to the system."""
    print("\n--- Add Contact ---")
    phone = input("Enter phone number: ").strip()

    if phone in contacts:
        print("Error: A contact with this phone number already exists.")
        return

    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()

    if not phone or not name:
        print("Error: Name and Phone number cannot be empty.")
        return

    contacts[phone] = {"name": name, "email": email}
    print(f"Contact for '{name}' added successfully!")


def edit_contact():
    """Modifies an existing contact's details."""
    print("\n--- Edit Contact ---")
    phone = input("Enter the phone number of the contact to edit: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    current = contacts[phone]
    print(
        f"Current details - Name: {current['name']}, Email: {current['email']}"
    )

    new_name = (
        input("Enter new name (leave blank to keep current): ").strip()
        or current["name"]
    )
    new_email = (
        input("Enter new email (leave blank to keep current): ").strip()
        or current["email"]
    )

    contacts[phone] = {"name": new_name, "email": new_email}
    print("Contact updated successfully!")


def delete_contact():
    """Removes a contact using their phone number."""
    print("\n--- Delete Contact ---")
    phone = input("Enter the phone number of the contact to delete: ").strip()

    if phone in contacts:
        removed = contacts.pop(phone)
        print(f"Deleted contact: {removed['name']}")
    else:
        print("Contact not found.")


def export_contacts():
    """Exports all contacts to a CSV file."""
    print("\n--- Export Contacts ---")
    if not contacts:
        print("No contacts available to export.")
        return

    filename = (
        input("Enter filename (default: contacts.csv): ").strip()
        or "contacts.csv"
    )

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Phone Number", "Name", "Email"])  # Header row
            for phone, info in contacts.items():
                writer.writerow([phone, info["name"], info["email"]])
        print(f"Successfully exported {len(contacts)} contacts to {filename}!")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")


def main():
    """Main program loop."""
    while True:
        print("\n=============================")
        print("  CONTACT MANAGEMENT SYSTEM  ")
        print("=============================")
        print("1. Add")
        print("2. Edit")
        print("3. Delete")
        print("4. Export")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            export_contacts()
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
