# ============================================================
# 04_predict.py - Credit Card Limit Tracker
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

credit_card_limit = 5000
transactions = []

while True:
    price = int(input('How much do you want to pay?\n'))
    if credit_card_limit >= sum(transactions) + price:
        print("Thanks for shopping with us!")  # Your prediction: Thanks for shopping with us!
        transactions.append(price)
    else:
        print('Sorry, your card got rejected!')  # Your prediction: Sorry, your card got rejected!
        break

print(f'You spend a total of {sum(transactions)} this month.')  # Your prediction: e.g. You spend a total of 4500 this month.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
