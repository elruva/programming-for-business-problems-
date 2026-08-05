# ============================================================
# 03_investigate.py - NameError with input()
# ============================================================
# This code has a bug! Find and fix it.
# ============================================================

# BUG: This code will crash with a NameError. Why?
joke = input("Tell me a joke: ")

print(f"You told the following joke: {joke}")

# Q1: What is wrong with this code?
# Answer: The answer is never stored, so the variable joke does not exist

# Q2: How do you fix it?
# Fix: joke = input("Tell me a joke: ")
