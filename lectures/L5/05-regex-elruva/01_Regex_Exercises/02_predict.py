# ============================================================
# 02_predict.py - Anchors (^ and $)
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import re

text = "This book on tennis cost $3.99 at Walmart."

reg2 = re.compile(r"$This")
match = reg2.search(text)
print(match)  # Your prediction: None

reg2 = re.compile(r"^This")
match = reg2.search(text)
print(match)  # Your prediction: <re.Match object; span=(0, 4), match='This'>

reg2 = re.compile(r"This^") #read This, then be at th start 
match = reg2.search(text)
print(match)  # Your prediction: None

reg2 = re.compile(r"This$") #read This, then be at the end
match = reg2.search(text)
print(match)  # Your prediction: None

reg2 = re.compile(r"Walmart\.$")
match = reg2.search(text)
print(match)  # Your prediction: <re.Match object; span=(34, 42), match='Walmart.'>

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================

#- ^ = "we are at the start of the string right now"
#- $ = "we are at the end of the string right now"
# \. - end with a real dot 

