# ============================================================
# 01_predict.py - While Loop with User Input
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

# Example: While loop with user input
answer = input("What is the capital of France?\n> ")

while answer != "Paris":
    print("Incorrect! Try again.")  # Your prediction: Incorrect! Try again.
    answer = input("What is the capital of France?\n> ")

print("Correct!")  # Your prediction: Correct!

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What condition keeps the loop running?
# Answer: answer != "Paris" - the loop runs while the answer is not Paris.

# Q2: What happens if you type "Paris" on the first try?
# Answer: The loop body never runs and it prints Correct! straight away.

# Q3: What happens if you type "paris" (lowercase)?
# Answer: It counts as wrong, because "paris" is not the same string as "Paris".

# Q4: Is this a definite or indefinite loop? Why?
# Answer: Indefinite, because we do not know how many wrong answers the user will type.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
