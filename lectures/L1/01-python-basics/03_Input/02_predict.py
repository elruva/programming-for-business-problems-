# ============================================================
# 02_predict.py - Input with prompts
# ============================================================
# PREDICT: What will this code output? Write your prediction below.
# ============================================================

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

print(f"Hi {firstName} {lastName}! How are you today?")

# MY PREDICTION:
# 1. It asks: Please enter your first name: and waits
# 2. It asks: Please enter your last name: and waits
# 3. It prints Hi <first> <last>! How are you today?


# ============================================================
# INVESTIGATE: Answer these questions after running the code.
# ============================================================

# Q1: What is the difference between input() and input("text")?
# Answer: input() shows nothing, input("text") shows a message first

# Q2: Why is there a space after "first name: "?
# Answer: So what you type does not stick to the colon

# Q3: How many times does the program wait for user input?
# Answer: Twice, once per input()
