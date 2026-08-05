# ============================================================
# 03_predict.py - Building a Dictionary with User Input
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

favorite_foods = {}

while True:
    name = input('Enter your name:\n>')
    food = input('Enter your favorite food:\n>')
    favorite_foods[name] = food
    again = input('Do you want to add another person?\n>')
    if again == 'no':
        break

for key in favorite_foods:
    print(f'{key} loves {favorite_foods[key]}')  # Your prediction: one line per person, e.g. Anna loves Pasta

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
