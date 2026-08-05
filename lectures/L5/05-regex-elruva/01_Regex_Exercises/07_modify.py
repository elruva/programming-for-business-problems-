# ============================================================
# 07_modify.py - URL Pattern Matching
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

import re

reg = re.compile(r"www.google.(de|com)")

m = reg.match("www.google.com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.au.dk")
print(m)

m = reg.match("www.bss.au.dk/economics/programmes/")
print(m)

# ============================================================
# TASKS
# ============================================================
# 1. Modify the regex pattern so it matches all four URLs above.
# 2. Make sure to properly escape the dots so "." is a literal dot
#    and not "any character".
# 3. Handle an optional http:// or https:// prefix at the start.

# ============================================================
# Write your improved code below:
# ============================================================
