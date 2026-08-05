# ============================================================
# 02_predict.py - Iterating Over Dictionary Items
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

sales = {'Mike': 150, 'Sandra': 320, 'Josh': 275, 'Anna': 190}

for name, amount in sales.items():
    print(f'{name}: ${amount}')  # Your prediction: Mike: $150, then Sandra: $320, Josh: $275, Anna: $190

print(f'Average: ${sum(sales.values()) / len(sales.values()):.2f}')  # Your prediction: Average: $233.75

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
