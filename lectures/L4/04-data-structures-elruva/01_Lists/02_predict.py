# ============================================================
# 02_predict.py - Building a List with User Input
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

prices = []

nItems = int(input('How many prices do you want to enter:\n>'))

for i in range(0, nItems):
    price = float(input("Please enter the next price:\n>"))
    prices.append(price)

print(prices)  # Your prediction: the list of the prices you typed, e.g. [10.0, 4.5]
print(f'Total: {sum(prices)}')  # Your prediction: Total: 14.5 - sum() adds all the prices

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
