# ============================================================
# 03_predict.py - Reading CSV with DictReader
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import csv

# DictReader reads CSV files and returns each row as a dictionary
# The first row of the CSV is used as keys (column headers)
# This makes it easier to access values by column name instead of index

with open('lectures/L4/04-data-structures-elruva/04_Files/mydata2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Your prediction: each row as a dictionary, e.g. {'Name': 'Niko', ' Phone': ' +491701231123', ' Email': ' nstein@test.de'}

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
