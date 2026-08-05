# ============================================================
# 05_investigate.py - Where Does the Match Happen?
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

import re

text = "Order shipped: invoice ready"

print(re.match(r"Order", text))
print(re.match(r"invoice", text))
print(re.search(r"invoice", text))
print(re.search(r"^invoice", text))
print(re.search(r"ready$", text))
print(re.search(r"READY$", text))

# ============================================================
# QUESTIONS
# ============================================================

# Q1: re.match(r"invoice", text) returns None, but
#     re.search(r"invoice", text) finds a match. Why?
# Answer:

# Q2: What does the ^ in r"^invoice" change compared to r"invoice"
#     when used with search() on this text?
# Answer:

# Q3: Why does r"READY$" return None even though the text ends
#     with the letters "ready"?
# Answer:
