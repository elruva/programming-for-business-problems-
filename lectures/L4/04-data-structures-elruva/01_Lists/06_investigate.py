# ============================================================
# 06_investigate.py - Sorting and Joining List Elements
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

letters = ['a', 'z', 'd', 'x', 'g', 'f']

letters.sort()

output = ''
for letter in letters:
    output += letter
print(output)

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What will be the output of the code?
# Answer: adfgxz - sort() puts the letters in order and the loop glues them into one string.