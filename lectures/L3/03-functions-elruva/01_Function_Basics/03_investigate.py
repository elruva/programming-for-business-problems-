# ============================================================
# 03_investigate.py - Function Basics: Parameters and Calls
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

def maths1():
    num1 = 50
    num2 = 5
    return num1 + num2

def maths2():
    num1 = 50
    num2 = 5
    return num1 - num2

def maths3(num1, num2):
    return num1 * num2

outputNum = maths2()
print(outputNum)

# ============================================================
# QUESTIONS
# ============================================================

# Q1: How many functions are there in the code?
# Answer: Three - maths1, maths2 and maths3.

# Q2: Which functions have parameters? How can you tell?
# Answer: Only maths3 - it has names inside its brackets, the others have empty brackets.

# Q3: Which functions are called in the code?
# Answer: Only maths2(), and it prints 45.

# Q4: What would happen if you called maths3() without any arguments?
# Answer: TypeError: maths3() missing 2 required positional arguments: 'num1' and 'num2'
