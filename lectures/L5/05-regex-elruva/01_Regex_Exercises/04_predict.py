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
print(m)  # Your prediction: <re.Match object; span=(0, 14), match='Hanna J Gruber'>
print(m.group(2))  # Your prediction: J

m = reg.match("Hanna Gruber")
print(m)  # Your prediction: <re.Match object; span=(0, 12), match='Hanna Gruber'>
print(m.group(4))  # Your prediction: Gruber

m = reg.match("Hanna Jana Gruber")
print(m)  # Your prediction: <re.Match object; span=(0, 10), match='Hanna Jana'> -> it stops as soon as it has enough
print(m.group(4))  # Your prediction: Jana

m = reg.match("Albert KD Klein")
print(m)  # Your prediction: <re.Match object; span=(0, 15), match='Albert KD Klein'>
print(m.group(2))  # Your prediction: KD

m = reg.match("Christoph M Flath")
print(m)  # Your prediction: <re.Match object; span=(0, 17), match='Christoph M Flath'>
print(m.group(2))  # Your prediction: M

m = reg.search("Hanna J Gruber, PhD")
print(m)  # Your prediction: <re.Match object; span=(0, 14), match='Hanna J Gruber'> -> the ", PhD" is simply not needed
print(m.group(2))  # Your prediction: J

m = reg.search("xw. Alfred Nobel")
print(m)  # Your prediction: <re.Match object; span=(4, 16), match='Alfred Nobel'> -> search skips the "xw. " at the start
print(m.group(2))  # Your prediction: an empty line, because [A-Z]* matched zero letters

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================

# Note:

# Each pair of () is one group, numbered from left to right:
#   group(0) = the whole match
#   group(1) = ([A-Z][a-z]+)   a capital letter and then small letters
#   group(2) = ([A-Z]*)        capital letters, * means zero or more
#   group(3) = ( )?            a space, ? means it is optional
#   group(4) = ([A-Z][a-z]+)   the last name

# Because group 2 uses * it is allowed to match nothing at all - then
# group(2) is an empty string and printing it gives an empty line.
