# ============================================================
# 03_investigate.py - Variable reassignment
# ============================================================
# Analyze this code carefully before running it.
# ============================================================

num1 = 20
num2 = 5

total = num1 + 15
total = num2 * 2
total = num1 - num2

print(f"Total is: {total}")

# Q1: What value does 'total' have after line 10?
# Answer: 35, because 20 + 15

# Q2: What value does 'total' have after line 11?
# Answer: 10, because 5 * 2

# Q3: What is the FINAL value of 'total' that gets printed?
# Answer: 15, because 20 - 5

# Q4: Why doesn't 'total' contain all three calculations?
# Answer: Each = replaces the old value, so only the last one is kept
