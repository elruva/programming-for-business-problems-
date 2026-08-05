# ============================================================
# 02_predict.py - Return Values: Print vs Return
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

def add_with_print(a, b):
    print(a + b)  # Your prediction: 7

def add_with_return(a, b):
    return a + b

# Test 1: Using the results
result1 = add_with_print(3, 4) #result 
result2 = add_with_return(3, 4) #no result --> because it's stored 

print(f"result1 = {result1}")  # Your prediction: no result, because print doesn't store the value 
print(f"result2 = {result2}")  # Your prediction: result2 = 7

# Test 2: Using in calculations
# total = add_with_print(5, 5) + 10  # Uncomment this - what happens?
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
total = add_with_return(5, 5) + 10
print(f"total = {total}")  # Your prediction: total = 20

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What is the difference between print() and return?
# Answer: print() only shows the value on screen, return hands it back so you can store and use it.

# Q2: Why is result1 equal to None?
# Answer: add_with_print has no return, so the call gives back None.

# Q3: Why can we do math with add_with_return() but not add_with_print()?
# Answer: One gives back a number, the other gives back None, and you cannot add None to 10.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
