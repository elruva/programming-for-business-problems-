# ============================================================
# 01_modify.py - Improve a greeting program
# ============================================================
# This program works, but it could be better. Your task is to improve it.
# ============================================================

name = "Student"
print("Hello " + name)
print("Welcome to Python programming!")

# ============================================================
# TASKS:
# ============================================================

# 1. Change the hardcoded name to ask the user for their name using input()

# 2. Use an f-string instead of string concatenation (+)

# 3. Add a third line that asks for the user's age and prints it

# 4. Add a fourth line that calculates and prints their birth year

# Write your improved code below:
name = input("What is your name? ")
print(f"Hello {name}!")

age = int(input("How old are you? "))
print(f"You are {age} years old.")

birthYear = 2026 - age
print(f"So you were born around {birthYear}.")
