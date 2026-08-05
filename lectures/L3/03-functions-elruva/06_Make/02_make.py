# ============================================================
# 02_make.py - Investment Calculator
# ============================================================
# MAKE: Create a program from scratch.
# This task combines all concepts from this session!
# ============================================================

# REQUIREMENTS:
# 1. get_positive_number(prompt) - Asks for a positive number.
#    - Use try/except to handle non-numeric input.
#    - Re-ask if the user enters 0 or a negative number.
#    - Keep asking until a valid number is entered.
#    - Returns the number as a float.
#
# 2. future_value(principal, years, rate=0.05) - Returns the final
#    amount after compound interest:
#        future_value = principal * (1 + rate) ** years
#    The rate parameter has a DEFAULT value of 0.05 (5% per year).
#
# 3. gain(principal, final_amount) - Returns the profit
#
# 4. display_summary(principal, years, rate, final_amount, profit)
#    - Prints a nicely formatted summary of the investment.
#
# Your program should:
# - Ask the user for the principal, years, and interest rate
#   (each input validated with get_positive_number).
# - Call future_value() and gain() with the user's numbers.
# - Display the summary.
# - Ask "Try another scenario? (y/n)" and loop until the user
#   answers "n".

# EXAMPLE OUTPUT:
#     === Investment Calculator ===
#     Enter principal in EUR: 1000
#     Enter number of years: 10
#     Enter annual interest rate (e.g. 0.05 for 5%): 0.07
#
#     === Summary ===
#     Principal:     1000.00 EUR
#     Years:         10.0
#     Rate:          7.00%
#     Future value:  1967.15 EUR
#     Gain:          967.15 EUR
#
#     Try another scenario? (y/n): n
#     Goodbye!

# This task combines:
# - Function definition with def
# - Parameters and DEFAULT parameter values
# - Return values
# - Error handling with try/except
# - Loops for replay

# ============================================================
# Write your code below:
# ============================================================

# Asks until the user types a number bigger than 0.
def get_positive_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            else:
                print("Values must be positive and not 0!")
        except ValueError:
            print("Invalid input! Please enter a number.")


# Only does the maths - it never asks anything.
def future_value(principal, years, rate=0.05):
    return principal * (1 + rate) ** years


def gain(principal, final_amount):
    return final_amount - principal


def display_summary(principal, years, rate, final_amount, profit):
    print("")
    print("=== Summary ===")
    print(f"Principal:     {principal:.2f} EUR")
    print(f"Years:         {years}")
    print(f"Rate:          {rate * 100:.2f}%")
    print(f"Future value:  {final_amount:.2f} EUR")
    print(f"Gain:          {profit:.2f} EUR")
    print("")


def ask_enter_again():
    answer = input("Try another scenario? (y/n): ")
    return answer == "y"


print("=== Investment Calculator ===")

while True:
    principal = get_positive_number("Enter principal in EUR: ")
    years = get_positive_number("Enter number of years: ")
    rate = get_positive_number("Enter annual interest rate (e.g. 0.05 for 5%): ")

    final_amount = future_value(principal, years, rate)
    profit = gain(principal, final_amount)
    display_summary(principal, years, rate, final_amount, profit)

    if not ask_enter_again():
        print("Goodbye!")
        break
