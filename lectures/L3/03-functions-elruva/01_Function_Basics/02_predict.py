# ============================================================
# 02_predict.py - Function Basics: Nested Function Calls
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

def greet_customer():
    print("Welcome to our store!")  
    show_menu()
    print("Have a nice day!")  

def show_menu():
    print("--- Menu ---") 
    print("1. Coffee")  
    print("2. Tea")  
    print("3. Juice")  
    print("------------")  

greet_customer() # your prediction: Welcome to our store! / --- Menu --- / 1. Coffee / 2. Tea / 3. Juice / ------------ / Have a nice day!

# ============================================================
# QUESTIONS
# ============================================================

# Q1: How many functions are defined?
# Answer: Two - greet_customer and show_menu.

# Q2: How many times is each function called?
# Answer: Each one is called once.

# Q3: Can a function call another function? What happens here?
# Answer: Yes - greet_customer stops in the middle and runs show_menu, then finishes its last print.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
