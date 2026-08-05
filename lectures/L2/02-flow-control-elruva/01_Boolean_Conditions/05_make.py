# ============================================================
# 05_make.py - Leap Year Checker
# ============================================================
# Build a program that checks whether a year is a leap year,
# using only Boolean expressions.
# ============================================================

# RULE:
# A year is a leap year if it is divisible by 4,
# except for century years (divisible by 100), which are NOT leap years,
# unless they are also divisible by 400.
#
# Examples:
# - 2024 -> True  (divisible by 4, not by 100)
# - 2023 -> False (not divisible by 4)
# - 1900 -> False (divisible by 100 but not by 400)
# - 2000 -> True  (divisible by 400)

# EXAMPLE OUTPUT:
# Enter a year: 2024
# Leap year: True

# Write your code below:

year = int(input('Year:'))

check4 = year % 4 == 0
check100 = year % 100 == 0
check400 = year % 400 == 0

leapYear = (check4 and not check100) or check400

print(f'The year {year} is a leap year: {leapYear}')