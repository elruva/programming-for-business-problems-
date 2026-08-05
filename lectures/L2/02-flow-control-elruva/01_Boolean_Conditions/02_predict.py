# ============================================================
# 02_predict.py - Complex Boolean Expressions
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

# Example 1
x = 50
y = 50
print(x + y == 100 and x >= y)  # Your prediction: True

# Example 2
x = 50
y = 50
print(x + y == 100 and x >= y and not y == 50)  # Your prediction: False - not y == 50 is False, so the whole and is False

# Example 3
fname = "Homer"
lname = "Simpson"
age = 66
print(fname + " " + lname == "Homer Simpson" and age > 55)  # " " - space 

# Example 4
x = 10
print(x > 10 or x < 10)  # Your prediction: False - x is exactly 10, so neither side is True

# Example 5
fname = "Homer"
lname = "Simpson"
print((fname == "Homer" and lname == "Homer") or (lname == "Simpson" and fname == "Homer"))  # Your prediction: True - the second bracket is True, and or only needs one

# Example 6
x = True
y = True
z = False
print(x or y or z)  # Your prediction: True

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
