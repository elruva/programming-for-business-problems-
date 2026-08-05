# ============================================================
# 02_predict.py - Split and Join Methods
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

data = "apple,banana,cherry,orange"

fruits = data.split(",")
print(fruits)  # Your prediction: ['apple', 'banana', 'cherry', 'orange']
print(fruits[0])  # Your prediction: apple
print(fruits[-1])  # Your prediction: orange

result = " - ".join(fruits)
print(result)  # Your prediction: apple - banana - cherry - orange

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
