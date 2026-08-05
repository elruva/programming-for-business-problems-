# ============================================================
# 06_make.py - Grade Calculator
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Ask the user to enter a test mark between 0 and 100
# 2. Validate the input:
#    - If the number is less than 0 or greater than 100, display an error
#    - Keep asking until a valid number is entered
# 3. Determine the grade:
#    - 90-100: "A" (Excellent)
#    - 80-89: "B" (Good)
#    - 70-79: "C" (Satisfactory)
#    - 60-69: "D" (Sufficient)
#    - Below 60: "F" (Fail)
# 4. Tell the user if a retake is required (grade F)

# EXAMPLE OUTPUT:
#     Enter your test mark (0-100): 75
#     Your grade: C (Satisfactory)
#     No retake required.
#
#     Enter your test mark (0-100): 45
#     Your grade: F (Fail)
#     A retake is required!

# ============================================================
# Write your code below:
# ============================================================

mark = int(input("Enter your test mark (0-100): "))

while mark < 0 or mark > 100:
    print("Error: the mark must be between 0 and 100.")
    mark = int(input("Enter your test mark (0-100): "))

if mark >= 90:
    print("Your grade: A (Excellent)")
elif mark >= 80:
    print("Your grade: B (Good)")
elif mark >= 70:
    print("Your grade: C (Satisfactory)")
elif mark >= 60:
    print("Your grade: D (Sufficient)")
else:
    print("Your grade: F (Fail)")

if mark < 60:
    print("A retake is required!")
else:
    print("No retake required.")








