# ============================================================
# 08_make.py - Product Recommendation System
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Create a list of at least 6 products (e.g., "Laptop", "Phone", "Tablet", etc.)
# 2. Create a list of corresponding prices for each product
# 3. Ask the user for their budget (as a number)
# 4. Find all products that are within the user's budget
# 5. If there are affordable products:
#    - Display them to the user
#    - Ask if they want a random recommendation or to pick themselves
#    - If random: randomly select one affordable product and display it
#    - If pick: let them enter a product name and confirm their choice
# 6. If no products are within budget, suggest the cheapest product

# EXAMPLE OUTPUT:
# Enter your budget: 500
# Affordable products: Phone, Tablet, Headphones
# Random recommendation or pick yourself? (r/p): r
# We recommend: Tablet

# Hint: Use the random module for random selection
# Hint: Use a loop to find products within budget

# ============================================================
# Write your code below:
# ============================================================

import random

products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor", "Keyboard"]
prices = [1200, 450, 300, 90, 250, 40]

budget = float(input("Enter your budget: "))

# Collect everything the user can afford
affordable = []
for i in range(len(products)):
    if prices[i] <= budget:
        affordable.append(products[i])

if len(affordable) > 0:
    print("Affordable products: " + ", ".join(affordable))
    how = input("Random recommendation or pick yourself? (r/p): ")
    if how.lower() == "r":
        print("We recommend: " + random.choice(affordable))
    else:
        pick = input("Which product do you want? ")
        if pick in affordable:
            print("Good choice: " + pick)
        else:
            print("Sorry, that product is not on your list.")
else:
    # Nothing affordable - suggest the cheapest product instead
    cheapest = products[0]
    cheapest_price = prices[0]
    for i in range(len(products)):
        if prices[i] < cheapest_price:
            cheapest = products[i]
            cheapest_price = prices[i]
    print(f"Nothing fits your budget. The cheapest product is {cheapest} at {cheapest_price}.")
