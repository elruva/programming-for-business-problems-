# ============================================================
# 02_predict.py - If/Else and If/Elif/Else Statements
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

# Example 1: if/else statement
num1 = 1337

if num1 == 10:
    print("This text is output because the condition was true")  # Your prediction: nothing, 1337 is not 10
else:
    print("This text is output because the condition was false")  # Your prediction: This text is output because the condition was false


# Example 2: if/elif/else statement
score = 75

if score >= 90:
    print("Grade: A")  # Your prediction: nothing, 75 is not >= 90
elif score >= 80:
    print("Grade: B")  # Your prediction: nothing, 75 is not >= 80
elif score >= 70:
    print("Grade: C")  # Your prediction: Grade: C
elif score >= 60:
    print("Grade: D")  # Your prediction: nothing, Python stops after the first true branch
else:
    print("Grade: F")  # Your prediction: nothing, the elif above was already true

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
