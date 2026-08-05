# ============================================================
# 04_modify.py - Expand the Guessing Game
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

# Original version (commented out so only the improved version below runs):
# import random
#
# randomNumber = random.randint(1, 50)
# guess = int(input("I selected a secret number between 1 and 50. Try to guess it:\n>"))
#
# while guess != randomNumber:
#     if guess < randomNumber:
#         guess = int(input("Wrong - your number is too small! Guess again.\n>"))
#     elif guess > randomNumber:
#         guess = int(input("Wrong - your number is too big! Guess again.\n>"))
#
# print(f"Good job! You guessed {randomNumber} correctly")

# ============================================================
# TASKS
# ============================================================
# 1. Ask the user for a username and greet them personally
# 2. Track the score (number of guesses needed)
# 3. Display the score at the end
# 4. Ask if they want to play again (use a while loop)
#
# Hint: You might want to create separate functions for:
# - Getting the username
# - Playing one round
# - Asking to play again

# ============================================================
# Write your improved code below:
# ============================================================


import random


def get_username():
    name = input("What is your username? ")
    return name


def play_round():
    secretNumber = random.randint(1, 50)
    counter = 0
    while True:
        guess = int(input("Guess a number between 1 and 50:\n>"))
        counter = counter + 1
        if guess < secretNumber:
            print("Too small! Try again.")
        elif guess > secretNumber:
            print("Too big! Try again.")
        else:
            print(f"Correct! The number was {secretNumber}.")
            return counter


def ask_play_again():
    answer = input("Do you want to play again? (yes/no)\n>")
    return answer == "yes"


def say_goodbye(name):
    print(f"Thanks for playing, {name}! See you next time.")


username = get_username()
print(f"Hi {username}! Let's play.")

while True:
    score = play_round()
    print(f"{username}, you needed {score} guesses.")
    if not ask_play_again():
        say_goodbye(username)
        break