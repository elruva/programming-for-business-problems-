# ============================================================
# 06_make.py - Number Guessing Game
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. The program thinks of a secret number (you can hardcode it or use random)
# 2. The user has to guess the number
# 3. After each guess, tell the user if their guess was:
#    - Too high
#    - Too low
#    - Correct!
# 4. Count the number of attempts
# 5. When the user guesses correctly, show:
#    - Congratulations message
#    - Number of attempts it took

# BONUS CHALLENGES:
# - Add a maximum number of attempts (e.g., 7)
# - Let the user choose the difficulty (range 1-10, 1-50, or 1-100)

# EXAMPLE OUTPUT:
#     Welcome to the Number Guessing Game!
#     I'm thinking of a number between 1 and 100.
#
#     Your guess: 50
#     Too high! Try again.
#
#     Your guess: 25
#     Too low! Try again.
#
#     Your guess: 37
#     Correct! You got it in 3 attempts!
# ============================================================
# Write your code below:
# ============================================================

number = int(input('Guess the number: '))
secretnumber = 57 
counter = 0


while True:
    number = int(input('Your guess: '))
    counter += 1
    if number > secretnumber:
        print ('Too high! Try again!')
    elif number < secretnumber:
        print ('Too low! Try again!')
    else:
        print (f'Correct! You got it in {counter} attempts!')
        break