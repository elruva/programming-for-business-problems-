# ============================================================
# 04_make.py - Create a restaurant tip calculator
# ============================================================
# Build a program that calculates the tip for a restaurant meal.
# ============================================================

# REQUIREMENTS:
# 1. Ask the user for the price of the meal (as a decimal, e.g., 45.50)
# 2. Ask the user for the tip percentage they want to give (e.g., 15 for 15%)
# 3. Calculate the tip amount
# 4. Calculate the total price (meal + tip)
# 5. Display the meal price, tip amount, and total price


# EXAMPLE OUTPUT:
# Enter the meal price: 45.50
# Enter tip percentage: 15
#
# Meal price: $45.50
# Tip (15%): $6.83
# Total: $52.33

# Write your code below:
price = float(input("Enter the meal price: "))
tipPercent = int(input("Enter tip percentage: ")) #no decimals 

tip = price * tipPercent / 100
total = price + tip

print(total)
print(f"Meal price: ${price:.2f}")
print(f"Tip ({tipPercent}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
