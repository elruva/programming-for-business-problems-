# ============================================================
# 03_predict.py - Groups, Alternation, and Escaping
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import re

reg = re.compile(r"www.google.de|com")
print(reg.match("www.google.com"))  # Your prediction:

reg = re.compile(r"www\.google\.(de|com)")
print(reg.match("www.google.de"))  # Your prediction:
print(reg.match("wwwwgoogle.de"))  # Your prediction:

string = "Niko Stein"

reg = re.compile(r"Nikolai Stein")
print(reg.match(string))  # Your prediction:

reg = re.compile(r"Niko Stein")
print(reg.match(string))  # Your prediction:

reg = re.compile(r"Niko|Nikolai Stein")
print(reg.match(string))  # Your prediction:

reg = re.compile(r"(Niko | Nikolai) Stein")
print(reg.match(string))  # Your prediction:

reg = re.compile(r"(Niko|Nikolai) Stein")
print(reg.match(string))  # Your prediction:

string = r"\."

reg = re.compile(r".")
print(reg.match(string))  # Your prediction:
print(reg.findall(string))  # Your prediction:

reg = re.compile(r"\.")
print(reg.match(string))  # Your prediction:
print(reg.search(string))  # Your prediction:

reg = re.compile(r"\\")
print(reg.match(string))  # Your prediction:

reg = re.compile(r"\\.")
print(reg.match(string))  # Your prediction:

reg = re.compile(r"\\\.")
print(reg.match(string))  # Your prediction:

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile(r"is")
match = re.findall(reg, text)
print(match)  # Your prediction:

reg = re.compile(r"\d")
match = re.findall(reg, text)
print(match)  # Your prediction:

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
