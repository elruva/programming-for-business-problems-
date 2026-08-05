# ============================================================
# 03_investigate.py - Multiplication Table Loop
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

number = 6
counter = 1

while counter < 11:
    print(counter * number)
    counter = counter + 1

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What is the iteration variable in this loop?
# Answer: counter - it changes on every pass and controls the condition.

# Q2: How many times does the loop run?
# Answer: 10 times, for counter 1 up to 10.

# Q3: What is the first number printed?
# Answer: 6

# Q4: What is the last number printed?
# Answer: 60

# Q5: What would happen if we removed "counter = counter + 1"?
# Answer: counter would stay 1 forever, so it would print 6 in an endless loop.
