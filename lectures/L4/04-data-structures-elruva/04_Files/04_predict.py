# ============================================================
# 04_predict.py - Writing to a Text File
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

data = ['Hello World', 'How are you?', '12345']

with open('lectures/L4/04-data-structures-elruva/04_Files/mydata.txt', 'w') as fileHandler:
    for line in data:
        fileHandler.write(line + '\n')

print("File written successfully!")  # Your prediction: File written successfully!

#end: overwrite the file with the new data


# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================

# open() modes:
#   'r'   read
#   'w'   write - wipes the file first
#   'a'   append
#   'x'   create, fails if it exists
#   'r+'  read and write
#   'w+'  write and read
#   'a+'  append and read
#   'rb'  binary
#   'wb'  binary
