# ============================================================
# 02_predict.py - Error Handling: Input Validation Loop
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

def get_number(prompt):
    while True:                 #more than one attempt (loop)
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("That's not a valid number! Try again.")  # Your prediction: That's not a valid number! Try again.

# Test 1: Enter a valid number (e.g., 25)
age = get_number("Enter your age: ")
print(f"You are {age} years old.")  # Your prediction: You are 25 years old.

# Test 2: Try entering "twenty" or "abc" first, then a number

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What happens when you enter "twenty" instead of a number?
# Answer: int() fails with a ValueError, so it prints the message and asks again.

# Q2: Why is there a while True loop?
# Answer: So it keeps asking until the user finally types a real number.

# Q3: When does the function return and exit the loop?
# Answer: As soon as int(input(...)) works, return hands the number back and ends the function.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
