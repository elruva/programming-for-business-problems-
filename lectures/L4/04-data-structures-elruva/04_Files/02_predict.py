# ============================================================
# 02_predict.py - Reading CSV with csv.reader
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import csv

with open('04_Files/mydata.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)  # Your prediction: each row as a list, e.g. ['Niko', ' +491701231123', ' nstein@test.de']

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
