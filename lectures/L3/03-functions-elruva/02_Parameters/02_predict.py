# ============================================================
# 02_predict.py - Parameters: Multiple Parameters and Return
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

def tip_calculator(price, percentage):
    tip = price * percentage
    total = price + tip
    print(f"You should tip {tip:.2f}€ and pay a total of {total:.2f}€!") 
    return tip, total

tipNew, totalNew = tip_calculator(25, 0.1) # Your prediction: You should tip 2.50€ and pay a total of 27.50€!
print(f"Saved tip: {tipNew:.2f}€")  # Your prediction: Saved tip: 2.50€

# ============================================================
# QUESTIONS
# ============================================================

# Q1: How many parameters does tip_calculator have?
# Answer: Two - price and percentage.

# Q2: What does the function return?
# Answer: Two values, the tip and the total.

# Q3: What does "tipNew, totalNew = ..." do?
# Answer: It puts the first returned value in tipNew and the second in totalNew.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
