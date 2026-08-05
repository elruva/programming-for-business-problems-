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
print(match)  # Your prediction:

reg2 = re.compile(r"^This")
match = reg2.search(text)
print(match)  # Your prediction:

reg2 = re.compile(r"This^")
match = reg2.search(text)
print(match)  # Your prediction:

reg2 = re.compile(r"This$")
match = reg2.search(text)
print(match)  # Your prediction:

reg2 = re.compile(r"Walmart\.$")
match = reg2.search(text)
print(match)  # Your prediction:

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
