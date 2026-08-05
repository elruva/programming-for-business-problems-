# ============================================================
# 07_modify.py - Product Data Cleaner
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

raw_lines = [
    "  laptop ; 999.99 ; 5  ",
    "MOUSE;29.99;50",
    "  Keyboard ; 79.99 ; 25  ",
    "monitor;299.99;10"
]

# Your code here:
products = []

# Process each line...

# Print formatted output like:
# Product: Laptop, Price: 999.99, Stock: 5

# ============================================================
# TASKS
# ============================================================
# 1. Remove leading/trailing whitespace from each line
# 2. Split each line by the semicolon separator
# 3. Clean each field (remove extra spaces)
# 4. Convert the product name to title case
# 5. Store the results in a list of dictionaries
# 6. Print a formatted summary

# ============================================================
# Write your improved code below:
# ============================================================

for line in raw_lines:
    parts = line.strip().split(";")
    product = {
        "name": parts[0].strip().title(),
        "price": float(parts[1].strip()),
        "stock": int(parts[2].strip())
    }
    products.append(product)

for product in products:
    print(f"Product: {product['name']}, Price: {product['price']}, Stock: {product['stock']}")
