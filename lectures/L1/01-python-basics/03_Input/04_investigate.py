# ============================================================
# 04_investigate.py - Combining input with string slicing
# ============================================================
# This code calculates initials from user input.
# ============================================================

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

fullName = firstName + " " + lastName
initials = firstName[0] + lastName[0]

print(f"Hi {fullName}. Your initials are {initials}!")

# Q1: What does firstName[0] return?
# Answer: The first letter of the first name

# Q2: Why do we use [0] instead of [1] to get the first letter?
# Answer: Because Python starts counting at 0

# Q3: What would initials look like if the user entered "homer" and "simpson"?
# Answer: hs - lowercase, because slicing copies the letters exactly as typed
