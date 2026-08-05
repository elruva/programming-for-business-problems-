# ============================================================
# 03_investigate.py - Error Handling: Multiple Exception Types
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# Run this code with different inputs and analyze the behavior.
# ============================================================

def safe_divide(a, b):
    try:                        #one attempt 
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Both values must be numbers!")
        return None

# Test cases
print("Test 1:", safe_divide(10, 2))
print("Test 2:", safe_divide(10, 0))
print("Test 3:", safe_divide("ten", 2))
print("Test 4:", safe_divide(10, "two"))

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What does Test 1 return?
# Answer: 5.0 - the division works, so no except block runs.

# Q2: What does Test 2 return and print?
# Answer: It prints "Error: Division by zero!" and returns None.

# Q3: What type of error occurs in Tests 3 and 4?
# Answer: TypeError, because you cannot divide a string and a number.

# Q4: Why is it useful to catch different error types separately?
# Answer: You can give a message that actually explains what went wrong.
