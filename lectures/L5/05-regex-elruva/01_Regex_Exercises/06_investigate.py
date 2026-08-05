# ============================================================
# 06_investigate.py - Greedy Matching, Optional Parts, and Sets
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

import re

# (a) Greedy matching
print(re.findall(r"\(.*\)", "(a) text (b) more (c)"))

# (b) Optional part
print(re.search(r"Dr\.? Smith", "Dr Smith"))
print(re.search(r"Dr\.? Smith", "Dr. Smith"))

# (c) A quantifier on a character set
print(re.findall(r"[A-Z]{2,}", "Python and SCM at AU"))

# ============================================================
# QUESTIONS
# ============================================================

# Q1: Why does r"\(.*\)" return one big match spanning from the first
#     "(" to the last ")", instead of three separate groups?
# Answer:

# Q2: What does the "?" after "\." mean in r"Dr\.? Smith", and why does
#     the pattern match both "Dr Smith" and "Dr. Smith"?
# Answer:

# Q3: What does r"[A-Z]{2,}" match? Explain why "Python" does not appear
#     as a whole in the result, and which substrings do.
# Answer:
