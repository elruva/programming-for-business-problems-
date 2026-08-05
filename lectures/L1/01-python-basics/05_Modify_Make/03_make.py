# ============================================================
# 03_make.py - Create a rectangle area calculator
# ============================================================
# Build a program from scratch that calculates the area of a rectangle.
# ============================================================

# REQUIREMENTS:
# 1. Ask the user for the width of the rectangle
# 2. Ask the user for the length (height) of the rectangle
# 3. Calculate the area (width * length)
# 4. Display the result in a nicely formatted message

# EXAMPLE OUTPUT:
# Enter the width: 5
# Enter the length: 10
# The area of a 5 x 10 rectangle is 50 square units.

# Write your code below:
width = float(input("Enter the width: "))
length = float(input("Enter the length: "))

area = width * length

print(f"The area of a {width} x {length} rectangle is {area} square units.")


# ============================================================
# ANOTHER WAY TO WRITE THE SAME THING
# This version is live too, so it asks for the size a second time.
# Comment it out once you have compared the two.
# ============================================================

# Option A - do the multiplication inside the f-string.
# Shorter, but harder to read once the sum gets bigger.
width = float(input("Enter the width: "))
length = float(input("Enter the length: "))
print(f"The area of a {width} x {length} rectangle is {width * length} square units.")
