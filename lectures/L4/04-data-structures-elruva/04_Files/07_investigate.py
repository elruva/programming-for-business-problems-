# ============================================================
# 07_investigate.py - File Opening Approaches
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

# Approach 1: Manual open/close
file1 = open('04_Files/mydata.txt', 'r')
content1 = file1.read()
file1.close()
print("Approach 1 done")

# Approach 2: Using 'with' statement
with open('04_Files/mydata.txt', 'r') as file2:
    content2 = file2.read()
print("Approach 2 done")

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What is the difference between Approach 1 and Approach 2?
# Answer: In the first you must close the file yourself, in the second "with" closes it for you.

# Q2: What happens if we forget file1.close() in Approach 1?
# Answer: The file stays open, and anything written to it may not be saved properly.

# Q3: Why is Approach 2 considered "better practice"?
# Answer: It always closes the file, even if an error happens in between.
