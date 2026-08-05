# ============================================================
# 01_predict.py - Return Values: Basic Return Statements
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

# print --> cannot be reused 
# return --> the value is returned and can be used (with print reuslts)


def maths1():
    num1 = 50
    num2 = 5
    return num1 + num2

def maths2():
    num1 = 50
    num2 = 5
    return num1 - num2

def maths3():
    num1 = 50
    num2 = 5
    return num1 * num2

outputNum = maths2()
print(outputNum)  # Your prediction: 45

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What value is stored in outputNum?
# Answer: 45, because maths2() returns 50 - 5.

# Q2: What would maths1() + maths3() return?
# Answer: 55 + 250 = 305

# Q3: What happens if a function doesn't have a return statement?
# Answer: It gives back None, so there is no value you can use.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
