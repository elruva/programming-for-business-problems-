# ============================================================
# 04_modify.py - Robust Temperature Converter
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

def get_temperature():
    while True:
        try:
            return float(input("Enter today's temperature in Celsius: "))
        except ValueError:
            print("That's not a valid number! Try again.")

def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temperature = get_temperature()
print(f"In Fahrenheit: {to_fahrenheit(temperature)}")

# ============================================================
# TASKS
# ============================================================
# 1. Run the code and type "warm" instead of a number.
#    What happens? Which exception is raised?
# 2. Add try/except inside get_temperature() so that a
#    ValueError is caught and an error message is printed.
# 3. Keep asking until the user enters a valid number
#    (use a while loop together with try/except).
# 4. Test by entering "abc" twice, then a valid number.

# ============================================================
# Write your improved code below:
# ============================================================

# Task 1: typing "warm" raises a ValueError:
# ValueError: could not convert string to float: 'warm'
# Tasks 2, 3 and 4 are already done by get_temperature() above - it catches
# the ValueError inside a while loop and keeps asking until the input works.

# Rounded version of the same result, so it is easier to read.
# (No second input() here - the temperature was already asked for above.)
print(f"{temperature} C is {to_fahrenheit(temperature):.1f} F")