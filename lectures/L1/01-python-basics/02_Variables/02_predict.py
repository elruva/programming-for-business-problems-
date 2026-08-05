# ============================================================
# 02_predict.py - Multiple variables and f-strings
# ============================================================
# PREDICT: What will this code output? Write your prediction below.
# ============================================================

firstName = "Homer"
lastName = "Simpson"
fullName = firstName + " " + lastName
age = 61

welcomeMessage = f"Hi! My name is {fullName} and I'm {age} years old."

print(welcomeMessage)

# MY PREDICTION:
# Hi! My name is Homer Simpson and I'm 61 years old.


# ============================================================
# INVESTIGATE: Answer these questions after running the code.
# ============================================================

# Q1: What does the + operator do when used with strings?
# Answer: It joins them together into one string

# Q2: What is the purpose of the 'f' before the quotation marks?
# Answer: It makes it an f-string, so variables in {} are filled in

# Q3: What do the curly braces {} do inside an f-string?
# Answer: They show where to put the value of a variable

# Q4: What happens if you change age from 61 to 39?
# Answer: The message says 39 years old instead of 61
