# ============================================================
# 05_modify.py - Ticket Price Calculator
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

age = int(input("Enter your age: "))

if age < 18:
    print("Child ticket: 5 EUR")
else:
    print("Adult ticket: 10 EUR")

# ============================================================
# TASKS
# ============================================================
# 1. Handle these pricing rules:
#    - Under 6: Free (0 EUR)
#    - 6-17: Child price (5 EUR)
#    - 18-64: Adult price (10 EUR)
#    - 65 and over: Senior price (7 EUR)
# 2. Add validation: if age is negative, print an error message

# ============================================================
# Write your improved code below:
# ============================================================

age = int(input("Enter your age: "))

if age <0:
    print("Error message")
elif age < 6:
    print("Free ticket: 0 EUR")
elif age <= 17:
    print("Child ticket: 5 EUR")
elif age <= 64:
    print("Adult price: 10 EUR")
else:
    print("Senior price: 7 EUR")

#elif --> one question, several possible answers
#if --> two  separate questions
