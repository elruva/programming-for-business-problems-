# ============================================================
# 05_predict.py - Writing CSV with DictWriter
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import csv

# DictWriter writes dictionaries to CSV files
# fieldnames specifies the column headers
# newline='' prevents extra blank lines on Windows

data = [
    {'name': 'John', 'age': 25},
    {'name': 'Sara', 'age': 27},
    {'name': 'Mike', 'age': 29}
]

keys = ['name', 'age']

with open('04_Files/newdata.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    for entry in data:
        writer.writerow(entry)

print("CSV file written successfully!")  # Your prediction: CSV file written successfully!

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
