# ============================================================
# 09_modify.py - Product Inventory Report
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

import csv

# Sample data - first create the CSV file
products = [
    {'product': 'Laptop', 'price': '999.99', 'quantity': '5'},
    {'product': 'Mouse', 'price': '29.99', 'quantity': '50'},
    {'product': 'Keyboard', 'price': '79.99', 'quantity': '25'},
    {'product': 'Monitor', 'price': '299.99', 'quantity': '10'}
]

# Write sample data to CSV
with open('products.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['product', 'price', 'quantity'])
    writer.writeheader()
    writer.writerows(products)

# ============================================================
# TASKS
# ============================================================
# 1. Read the products.csv file (you need to create it first with sample data)
# 2. Calculate the total value of all inventory (price * quantity for each product)
# 3. Find the most expensive product
# 4. Write a summary report to a file called 'report.txt'

# Sample products.csv content to create:
# product,price,quantity
# Laptop,999.99,5
# Mouse,29.99,50
# Keyboard,79.99,25
# Monitor,299.99,10

# ============================================================
# Write your improved code below:
# ============================================================

# Read the file back in - every value from a CSV arrives as text
rows = []
with open('products.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)

total_value = 0
most_expensive = rows[0]
for row in rows:
    total_value = total_value + float(row['price']) * int(row['quantity'])
    if float(row['price']) > float(most_expensive['price']):
        most_expensive = row

print(f"Total inventory value: {total_value:.2f}")
print(f"Most expensive product: {most_expensive['product']} ({most_expensive['price']})")

with open('report.txt', 'w') as file:
    file.write("Inventory report\n")
    file.write(f"Total inventory value: {total_value:.2f}\n")
    file.write(f"Most expensive product: {most_expensive['product']} ({most_expensive['price']})\n")

print("Report written to report.txt")
