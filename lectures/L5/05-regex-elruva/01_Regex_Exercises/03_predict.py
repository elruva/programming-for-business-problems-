# ============================================================
# 03_predict.py - Groups, Alternation, and Escaping
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import re

reg = re.compile(r"www.google.de|com")
print(reg.match("www.google.com"))  # Your prediction: None -> the | splits the WHOLE pattern into "www.google.de" or "com"

reg = re.compile(r"www\.google\.(de|com)")
print(reg.match("www.google.de"))  # Your prediction: <re.Match object; span=(0, 13), match='www.google.de'>
print(reg.match("wwwwgoogle.de"))  # Your prediction: None -> \. needs a real dot and there is a w there

string = "Niko Stein"

reg = re.compile(r"Nikolai Stein")
print(reg.match(string))  # Your prediction: None -> the text says Niko, not Nikolai

reg = re.compile(r"Niko Stein")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 10), match='Niko Stein'>

reg = re.compile(r"Niko|Nikolai Stein")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 4), match='Niko'> -> the choice is "Niko" or "Nikolai Stein"

reg = re.compile(r"(Niko | Nikolai) Stein")
print(reg.match(string))  # Your prediction: None -> the spaces inside the brackets are real characters

reg = re.compile(r"(Niko|Nikolai) Stein")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 10), match='Niko Stein'>

string = r"\."

reg = re.compile(r".")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 1), match='\\'> -> . takes the backslash
print(reg.findall(string))  # Your prediction: ['\\', '.'] -> every single character

reg = re.compile(r"\.")
print(reg.match(string))  # Your prediction: None -> the string starts with a backslash, not a dot
print(reg.search(string))  # Your prediction: <re.Match object; span=(1, 2), match='.'>

reg = re.compile(r"\\")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 1), match='\\'>

reg = re.compile(r"\\.")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 2), match='\\.'>

reg = re.compile(r"\\\.")
print(reg.match(string))  # Your prediction: <re.Match object; span=(0, 2), match='\\.'>

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile(r"is")
match = re.findall(reg, text)
print(match)  # Your prediction: ['is', 'is'] -> from "This" and from "tennis"

reg = re.compile(r"\d")
match = re.findall(reg, text)
print(match)  # Your prediction: ['3', '9', '9'] -> \d takes one digit at a time

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================

# r"." = any one character
# r"\." = a literal dot
# r"\\" = a literal backslash
# r"\\." = a backslash, then any character
# r"\\\." = a backslash, then a literal dot
#

# () groups things together, | chooses between the alternatives.
# Without the brackets the | splits the whole pattern, so write (de|com).

# A space inside a pattern is a normal character - never add spaces just to
# make a pattern look tidier.

# findall() gives back a plain list of the matched pieces, not a match object.
