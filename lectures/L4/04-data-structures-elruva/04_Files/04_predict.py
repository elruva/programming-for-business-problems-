# ============================================================
# 04_predict.py - Writing to a Text File
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

data = ['Hello World', 'How are you?', '12345']

with open('04_Files/newdata.txt', 'w') as fileHandler:
    for line in data:
        fileHandler.write(line + '\n')

print("File written successfully!")  # Your prediction: File written successfully!

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
