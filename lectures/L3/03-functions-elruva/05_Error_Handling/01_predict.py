# ============================================================
# 01_predict.py - Error Handling: Try/Except Basics
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

def divide(a, b):
    return a / b

# Option 1 - left commented out, it stops the program:
# ZeroDivisionError: division by zero
# result = divide(10, 0)
# print(f"Result: {result}")

# Option 2
try:
    result = divide(10, 0)
    print(f"Result: {result}")  
except ZeroDivisionError: #paste error type 
    print("Error: Cannot divide by zero!") 

print("Program continues running...")  # Your prediction: Program continues running...

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What error occurs when dividing by zero?
# Answer: ZeroDivisionError: division by zero

# Q2: What does try/except do?
# Answer: try runs the risky code, and except runs instead if that code fails.

# Q3: Why does "Program continues running..." still print?
# Answer: Because the error was caught, so the program does not stop.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
