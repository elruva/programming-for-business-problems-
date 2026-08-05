# ============================================================
# 03_investigate.py - Number Comparison
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

if number1 > number2:
    print("Number 1 is bigger than number 2")
elif number2 > number1:
    print("Number 2 is bigger than number 1")
else:
    print("Both numbers are the same")

# ============================================================
# QUESTIONS
# ============================================================

# Q1: Which keyword starts the selection?
# Answer: The keyword if.

# Q2: How many selection statements are there in the code?
# Answer: One, made of if, elif and else together.

# Q3: How many conditions are there in the code?
# Answer: Two, one after if and one after elif. else has no condition.

# Q4: What does the > operator mean?
# Answer: "Greater than", so it is only True when the left side is bigger.

# Q5: Why are the print statements indented?
# Answer: The indent shows which branch they belong to, so only that one runs.

# Q6: What happens if both numbers are equal?
# Answer: Both conditions are False, so else runs and prints "Both numbers are the same".
