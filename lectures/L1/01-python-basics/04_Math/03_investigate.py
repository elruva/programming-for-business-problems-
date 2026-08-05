# ============================================================
# 03_investigate.py - Type conversion with input()
# ============================================================
# This code has a bug! Find and fix it.
# ============================================================

num1 = 10
num2 = int(input("Please enter a number: "))

result = num1 + num2

print(f"Your result is: {result}")

# Q1: What error do you get when you run this code?
# Answer: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Q2: Why does this error occur?
# Answer: input() gives back a string, and a number cannot be added to text

# Q3: How do you fix it?
# Fix: num2 = int(input("Please enter a number: "))
