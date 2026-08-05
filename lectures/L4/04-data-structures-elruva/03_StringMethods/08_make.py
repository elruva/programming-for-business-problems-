# ============================================================
# 08_make.py - Email Validator
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Ask the user to enter an email address
# 2. Clean the input (strip whitespace, convert to lowercase)
# 3. Check if the email contains "@" and "."
# 4. If valid, add to a list of subscribers
# 5. If the email already exists in the list, show a message
# 6. Ask if they want to add another email (y/n)
# 7. At the end, show all subscribers joined by commas

# EXAMPLE OUTPUT:
# Enter email: JOHN@mail.com
# Email added!
# Add another? (y/n): y
# Enter email:   sara@mail.com
# Email added!
# Add another? (y/n): n
# Subscribers: john@mail.com, sara@mail.com

# ============================================================
# Write your code below:
# ============================================================

subscribers = []

while True:
    email = input("Enter email: ").strip().lower()

    if "@" in email and "." in email:
        if email in subscribers:
            print("That email is already on the list!")
        else:
            subscribers.append(email)
            print("Email added!")
    else:
        print("That does not look like an email address.")

    again = input("Add another? (y/n): ")
    if again.lower() != "y":
        break

print("Subscribers: " + ", ".join(subscribers))
