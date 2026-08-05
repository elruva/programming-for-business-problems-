# ============================================================
# 05_modify.py - Add more prompts
# ============================================================
# The starter code below asks for the user's name. Extend it so that
# it also asks for:
#   1. The user's city
#   2. The user's favorite color
# Then print a sentence that uses all three values.
# ============================================================

name = input("What is your name? ")

print(f"Hi {name}!")

# Write your extended code below:
city = input("What city do you live in? ")
color = input("What is your favorite color? ")

print(f"Hi {name}! You live in {city} and your favorite color is {color}.")


# ============================================================
# OTHER WAYS TO WRITE THE SAME THING
# All versions below are live, so the sentence is printed several
# times. That is on purpose - compare the code, not the output.
# ============================================================

# Option A - one sentence per line instead of one long sentence.
print(f"Hi {name}!")
print(f"You live in {city}.")
print(f"Your favorite color is {color}.")

# Option B - build the sentence in a variable first, then print it.
message = f"Hi {name}! You live in {city} and your favorite color is {color}."
print(message)
