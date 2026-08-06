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
# Answer: match() only looks at the very start of the string, and the text
#         starts with "Order", while search() keeps looking further along and
#         finds "invoice" at position 15.

# Q2: What does the ^ in r"^invoice" change compared to r"invoice"
#     when used with search() on this text?
# Answer: The ^ says the word must be at the start of the string, so search()
#         is no longer allowed to look further along and returns None.

# Q3: Why does r"READY$" return None even though the text ends
#     with the letters "ready"?
# Answer: Regular expressions are case-sensitive, so the capital letters in
#         READY do not match the small letters in "ready".
