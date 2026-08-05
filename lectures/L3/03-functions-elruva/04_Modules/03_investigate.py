# ============================================================
# 03_investigate.py - Modules: Number Guessing Game
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

import random

randomNumber = random.randint(1, 50)
guess = int(input("I selected a secret number between 1 and 50. Try to guess it:\n>")) #\n> - new line 

while guess != randomNumber:
    if guess < randomNumber:
        guess = int(input("Wrong - your number is too small! Guess again.\n>"))
    elif guess > randomNumber:
        guess = int(input("Wrong - your number is too big! Guess again.\n>"))

print(f"Good job! You guessed {randomNumber} correctly")

# ============================================================
# QUESTIONS
# ============================================================

# Q1: Which functions from modules are used in this program?
# Answer: random.randint() from the random module.

# Q2: Which built-in functions (not from modules) are used?
# Answer: input(), int() and print().

# Q3: How many times are the module functions called?
# Answer: Once - random.randint() runs one time, at the start.

# Q4: What would happen if we removed "import random"?
# Answer: NameError: name 'random' is not defined, because Python would not know that name.
