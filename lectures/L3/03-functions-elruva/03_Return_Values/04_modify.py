# ============================================================
# 04_modify.py - From print to return
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

def calculate_area(length, width):
    print(length * width)

area = calculate_area(5, 3)
print(f"Total area: {area}")

# ============================================================
# TASKS
# ============================================================
# 1. The line "Total area: None" is wrong. Change calculate_area
#    so it RETURNS the area instead of printing it.
# 2. Verify the second print now shows the correct value.
# 3. Add a function calculate_perimeter(length, width) that
#    returns the perimeter of the rectangle.
# 4. Call both functions for a 5 by 3 rectangle and print
#    the area and the perimeter.

# ============================================================
# Write your improved code below:
# ============================================================


def calculate_area(length, width):
    return(length * width)

def calculate_perimeter(length, width):
    return 2 * (length + width)

# lenght = 5
# width = 3 

area = calculate_area(5, 3)
perimmeter = calculate_perimeter(5, 3)

print(f"Total area: {area}")
print(f"Total perimeter: {perimmeter}")

