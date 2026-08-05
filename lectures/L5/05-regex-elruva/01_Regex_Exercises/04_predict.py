# ============================================================
# 04_predict.py - Capture Groups with Names
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import re

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile(r"([A-Z][a-z]+) ([A-Z]*)( )?([A-Z][a-z]+)")
m = reg.match("Hanna J Gruber")
print(m)  # Your prediction:
print(m.group(2))  # Your prediction:

m = reg.match("Hanna Gruber")
print(m)  # Your prediction:
print(m.group(4))  # Your prediction:

m = reg.match("Hanna Jana Gruber")
print(m)  # Your prediction:
print(m.group(4))  # Your prediction:

m = reg.match("Albert KD Klein")
print(m)  # Your prediction:
print(m.group(2))  # Your prediction:

m = reg.match("Christoph M Flath")
print(m)  # Your prediction:
print(m.group(2))  # Your prediction:

m = reg.search("Hanna J Gruber, PhD")
print(m)  # Your prediction:
print(m.group(2))  # Your prediction:

m = reg.search("xw. Alfred Nobel")
print(m)  # Your prediction:
print(m.group(2))  # Your prediction:

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
