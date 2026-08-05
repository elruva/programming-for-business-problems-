# ============================================================
# 01_predict.py - Reading a Text File Line by Line
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

with open('04_Files/mydata.txt') as fileHandler:
    for line in fileHandler:
        print(line.strip())  # Your prediction: the 4 lines of mydata.txt, e.g. Niko, +491701231123, nstein@test.de

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
