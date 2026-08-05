# ============================================================
# 01_predict.py - Counting Items with Dictionaries
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

meals = ['Pasta', 'Pizza', 'Kebab', 'Pasta', 'Salad', 'Burger', 'Burger', 'Pizza', 'Pasta']

counts = {}
for meal in meals:
    counts[meal] = counts.get(meal, 0) + 1

print(counts)  # Your prediction: {'Pasta': 3, 'Pizza': 2, 'Kebab': 1, 'Salad': 1, 'Burger': 2}

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
