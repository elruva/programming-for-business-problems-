# ============================================================
# 02_modify.py - Fix and improve a simple calculator
# ============================================================
# This calculator has bugs and is incomplete. Fix and extend it!
# ============================================================

# Current (buggy) code:
# print("Simple Calculator")
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
#
# result = num1 + num2
# print("The sum is: " + result)

# ============================================================
# TASKS:
# ============================================================

# 1. Fix the bug: the calculator is concatenating strings instead of adding numbers

# 2. Change the output to use an f-string instead of string concatenation

# 3. Add subtraction: calculate and display num1 - num2

# 4. Add multiplication: calculate and display num1 * num2

# 5. Add division: calculate and display num1 / num2

# Write your improved code below:
print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"The sum is: {num1 + num2}")
print(f"The difference is: {num1 - num2}")
print(f"The product is: {num1 * num2}")
print(f"The quotient is: {num1 / num2}")
