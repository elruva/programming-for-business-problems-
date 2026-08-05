# ============================================================
# 03_investigate.py - ECTS Thesis Requirement Check
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

# The following code checks if a student has enough ECTS to write the Bachelor thesis
min_points = 120
points = int(input("How many ECTS points do you already have? "))

allowed = points >= min_points

print("Allowed to write thesis:", allowed)

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What type of value does the variable 'allowed' hold?
# Answer: A boolean, so either True or False.

# Q2: What operator is used in the condition?
# Answer: >= which means "greater than or equal to".

# Q3: If a student has exactly 120 points, what will 'allowed' be?
# Answer: True, because >= also counts being exactly equal.

# Q4: If a student has 119 points, what will 'allowed' be?
# Answer: False, because 119 is under the 120 needed.
