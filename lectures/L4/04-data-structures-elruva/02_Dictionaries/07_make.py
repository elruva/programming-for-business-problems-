# ============================================================
# 07_make.py - Phone Book Application
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Create an empty list called phoneBook
# 2. Implement a menu system where the user can press:
#    - 1: Add an entry to the phonebook (name, phone number, email)
#         Store it in the list (you might want to use a nested dictionary)
#    - 2: Show all available contacts
#    - 3: Ask the user for a contact name and show all information for this contact
#    - 4: Terminate the program

# EXAMPLE OUTPUT:
# Press 1 to add, 2 to show all, 3 to search, 4 to exit: 1
# Enter name: John
# Enter phone: 555-1234
# Enter email: john@mail.com
# Contact added!
# Press 1 to add, 2 to show all, 3 to search, 4 to exit: 3
# Enter name to search: John
# Name: John, Phone: 555-1234, Email: john@mail.com

# ============================================================
# Write your code below:
# ============================================================

phoneBook = []

while True:
    choice = input("Press 1 to add, 2 to show all, 3 to search, 4 to exit: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        # One dictionary per contact, stored in the list
        contact = {"name": name, "phone": phone, "email": email}
        phoneBook.append(contact)
        print("Contact added!")

    elif choice == "2":
        if len(phoneBook) == 0:
            print("The phone book is empty.")
        else:
            for contact in phoneBook:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

    elif choice == "3":
        wanted = input("Enter name to search: ")
        found = False
        for contact in phoneBook:
            if contact["name"] == wanted:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                found = True
        if not found:
            print("No contact with that name.")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
