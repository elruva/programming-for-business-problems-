# ============================================================
# 04_investigate.py - String + Number confusion
# ============================================================
# What is the difference between these two expressions?
# ============================================================

print("5" + "3")  # Line 7: String concatenation
print(5 + 3)      # Line 8: Integer addition

# Q1: What does "5" + "3" produce on line 7?
# Answer: 53 - the two texts are joined

# Q2: What does 5 + 3 produce on line 8?
# Answer: 8 - the two numbers are added

# Q3: Why does Python treat these two cases differently?
# Answer: The quotes make them strings, and + joins strings but adds numbers
