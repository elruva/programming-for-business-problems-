# ============================================================
# 01_predict.py - Modules: Random Module and Dice Game
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# (Note: random values will vary!)
# ============================================================

import random

def roll_dice(sides=6):
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)

def play_round(player_name):
    """Play one round - roll two dice and return the total."""
    roll1 = roll_dice()
    roll2 = roll_dice()
    total = roll1 + roll2
    print(f"{player_name} rolled {roll1} and {roll2} = {total}")  # Your prediction: e.g. Homer rolled 5 and 2 = 7 (changes every run)
    return total

# Play a game
score_homer = play_round("Homer")
score_marge = play_round("Marge")

if score_homer > score_marge:
    print("Homer wins!")  # Your prediction: only if Homer's total is bigger
elif score_marge > score_homer:
    print("Marge wins!")  # Your prediction: only if Marge's total is bigger
else:
    print("It's a tie!")  # Your prediction: only if both totals are the same

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What module did we import? What function from it do we use?
# Answer: The random module, and we use random.randint().

# Q2: What is the default value for the "sides" parameter?
# Answer: 6, so a normal dice if you do not say otherwise.

# Q3: How do the two functions work together?
# Answer: play_round calls roll_dice twice and adds the two rolls into a total.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
