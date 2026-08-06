# ============================================================
# 01_predict.py - Match vs Search Methods
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import re

text = "This book on tennis cost $3.99 at Walmart."

reg1 = re.compile(r"ten")
match = reg1.match(text)
print(match)  # Your prediction: None

reg2 = re.compile(r"this")
match = reg2.match(text)
print(match)  # Your prediction: None

reg3 = re.compile(r"This")
match = reg3.match(text)
print(match)  # Your prediction: <re.Match object; span=(0, 4), match='This'>  

match = reg1.search(text)
print(match)  # Your prediction: <re.Match object; span=(13, 16), match='ten'> --> number means start with 13 and end with 16 (letters = positions)

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================

#Note:

#reg1.match(text) → match the begginning of the string (0) 

#reg1.search(text) → match the first occurence of the pattern in the string 



