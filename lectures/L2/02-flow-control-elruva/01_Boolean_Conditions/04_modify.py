# ============================================================
# 04_modify.py - Extend the thesis check
# ============================================================
# The starter code below checks if a student has enough ECTS
# to write the Bachelor thesis. Extend it for the tasks below.
# ============================================================

#\n - print lin


min_points = 120
points = int(input("How many ECTS points do you already have?\n"))

allowed = points >= min_points

print("Allowed to write thesis:", allowed)

# ============================================================
# TASKS
# ============================================================
# Assume the student also needs at least one completed internship.
# Ask for internships_completed and extend the condition so that
# both requirements must be met.

internship = int(input("How many internships have you completed?\n"))

allowed = allowed and internship >=1

print("Allowed to write thesis", allowed)


