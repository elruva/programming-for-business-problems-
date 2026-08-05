# ============================================================
# 03_investigate.py - Return Values and Variable Scope
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# This code has a bug! Find it and explain why it happens.
# ============================================================

def add_five(number):
    result = number + 5
    return result

number = 10

print(add_five(number))
# print(result)   # this is the bug - it stops the program with a NameError

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What output do you expect from print(add_five(number))?
# Answer: 15

# Q2: Why does print(result) cause an error?
# Answer: NameError: name 'result' is not defined - result only lives inside the function.

# Q3: Where does the variable "result" exist?
# Answer: Only inside add_five, it is a local variable and disappears when the function ends.

# Q4: How would you fix this code to print the result?
# Answer: Store what the function returns in a variable outside, then print that:
answer = add_five(number)
print(answer)
