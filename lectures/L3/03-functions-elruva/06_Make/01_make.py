# ============================================================
# 01_make.py - Grade Calculator
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. calculate_grade(score) - Takes a score (0-100) and returns the grade:
#    - 90-100: "A" (Excellent)
#    - 80-89: "B" (Good)
#    - 70-79: "C" (Satisfactory)
#    - 60-69: "D" (Sufficient)
#    - Below 60: "F" (Fail)
#
# 2. get_score() - Asks the user for a score, validates it's between 0-100
#    - Use try/except to handle non-numeric input
#    - Keep asking until valid input is given
#
# 3. display_result(score, grade) - Prints a formatted result message
#
# Your program should:
# - Get a score from the user (with validation)
# - Calculate and display the grade
# - Ask if they want to enter another score

# EXAMPLE OUTPUT:
#     Enter score (0-100): 85
#     Score: 85 -> Grade: B (Good)
#     Enter another score? (y/n): y
#     Enter score (0-100): abc
#     Invalid input! Please enter a number.
#     Enter score (0-100): 150
#     Score must be between 0 and 100!
#     Enter score (0-100): 72
#     Score: 72 -> Grade: C (Satisfactory)

#if --> condition needs to be satisfied (all 4)
#elfi --> python stops at the first True and skips the rest 


# ============================================================
# Write your code below:
# ============================================================

def calculate_grade(score):
    if score >= 90:
        return "A (Excellent)"
    elif score >= 80:
        return "B (Good)"
    elif score >= 70:
        return "C (Satisfactory)"
    elif score >= 60:
        return "D (Sufficient)"
    else:
        return "F (Fail)"


def get_score(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0 and num <= 100:
                return num
            else:
                print("Score must be between 0 and 100!")
        except ValueError:
            print("Invalid input! Please enter a number.")


def display_result(score, grade):
    print(f"Score: {score} -> Grade: {grade}")


def ask_enter_again():
    answer = input("Enter another score? (y/n): ")
    return answer == "y"


while True:
    score = get_score("Enter score (0-100): ")
    grade = calculate_grade(score)
    display_result(score, grade)
    if not ask_enter_again():
        break
