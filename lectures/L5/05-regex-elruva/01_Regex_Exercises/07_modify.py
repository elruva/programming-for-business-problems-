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

# (https?://)? = an optional http:// or https:// at the start, the ? after
#                the s means the s itself is optional too
# www\.        = the letters www and a REAL dot
# (\w+\.)+     = one or more "word plus dot" blocks, like "bss." and "au."
# \w+          = the last part of the domain, like com or dk

reg = re.compile(r"(https?://)?www\.(\w+\.)+\w+")

print(reg.match("www.google.com"))
print(reg.match("https://www.youtube.com"))
print(reg.match("http://www.au.dk"))
print(reg.match("www.bss.au.dk/economics/programmes/"))


# ============================================================
# OTHER WAYS TO WRITE THE SAME THING
# Uncomment one at a time (remove the #) and run it.
# Remember to comment out the active version above, or the output repeats.
# ============================================================

# Option A - spell out the two prefixes instead of using s?
# reg = re.compile(r"(http://|https://)?www\.(\w+\.)+\w+")

# Option B - a character set for the domain instead of \w and a dot.
#            [\w.]+ means "word characters and dots, one or more".
# reg = re.compile(r"(https?://)?www\.[\w.]+")
