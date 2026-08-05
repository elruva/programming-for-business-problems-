# ============================================================
# 08_investigate.py - File Reading Methods Comparison
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

# Reading all content vs line by line
with open('04_Files/mydata.txt', 'r') as file:
    # Method 1: Read entire file as one string
    all_content = file.read()
    print(f"Method 1 - Character count: {len(all_content)}")

# Note: We need to open again because we already read to the end
with open('04_Files/mydata.txt', 'r') as file:
    # Method 2: Read all lines into a list
    all_lines = file.readlines()
    print(f"Method 2 - Line count: {len(all_lines)}")

with open('04_Files/mydata.txt', 'r') as file:
    # Method 3: Iterate line by line
    count = 0
    for line in file:
        count += 1
    print(f"Method 3 - Line count: {count}")

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What is the difference between read() and readlines()?
# Answer: read() gives the whole file as one string, readlines() gives a list with one line per item.

# Q2: Why do we need to open the file again before each method?
# Answer: After reading, we are at the end of the file, so reading again would give nothing.