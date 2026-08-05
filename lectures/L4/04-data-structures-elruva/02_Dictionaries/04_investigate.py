# ============================================================
# 04_investigate.py - Combining Lists into a Dictionary
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

names = ['Sara', 'Mike', 'Julia', 'Sven']
attending = [True, False, False, True]

class_attendance = {}
for i in range(0, len(names)):
    class_attendance[names[i]] = attending[i]

print(class_attendance)

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What does the program do?
# Answer: It builds a dictionary where each name is a key and its True/False is the value.

# Q2: What will happen if we have two students with the same name?
# Answer: Keys must be unique, so the second one overwrites the first.
