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
print(match)  # Your prediction:

reg2 = re.compile(r"this")
match = reg2.match(text)
print(match)  # Your prediction:

reg3 = re.compile(r"This")
match = reg3.match(text)
print(match)  # Your prediction:

match = reg1.search(text)
print(match)  # Your prediction:

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
