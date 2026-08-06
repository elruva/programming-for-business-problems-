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
# Answer: .* is greedy, so it takes as many characters as it can and only then
#         looks for the closing bracket, which it finds at the very last ")".
#         Writing .*? instead makes it stop early and gives three matches.

# Q2: What does the "?" after "\." mean in r"Dr\.? Smith", and why does
#     the pattern match both "Dr Smith" and "Dr. Smith"?
# Answer: The ? makes the dot in front of it optional, so the pattern accepts
#         either zero dots or one dot after "Dr".

# Q3: What does r"[A-Z]{2,}" match? Explain why "Python" does not appear
#     as a whole in the result, and which substrings do.
# Answer: It matches two or more capital letters in a row, so it finds "SCM"
#         and "AU". "Python" has only one capital letter, the P, and one is
#         not enough for {2,}.
