# ============================================================
# 09_make.py - Hashtag and Mention Extractor
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

import re

captions = [
    "Loving the new release! #python #coding @data_driven",
    "Workshop today @aarhusuni - bring questions #AUCTP",
    "No tags here, just plain text",
    "Big thanks @alice and @bob #teamwork #fun",
]

# REQUIREMENTS:
# 1. For each caption, extract ALL #hashtags into one list and ALL
#    @mentions into another list (use re.findall).
# 2. A hashtag starts with '#' and a mention starts with '@', each
#    followed by one or more word characters.
# 3. Print each caption together with its hashtags and its mentions.
# 4. At the end, print the total number of hashtags found across all captions.

# EXAMPLE OUTPUT:
# Caption: Loving the new release! #python #coding @data_driven
#   Hashtags: ['#python', '#coding']
#   Mentions: ['@data_driven']
# ...
# Total hashtags: 5

# Hint: r"#\w+" finds the hashtags - what is the equivalent for mentions?

# ============================================================
# Write your code below:
# ============================================================

total = 0

for caption in captions:
    hashtags = re.findall(r"#\w+", caption)
    mentions = re.findall(r"@\w+", caption)
    print("Caption:", caption)
    print("  Hashtags:", hashtags)
    print("  Mentions:", mentions)
    total = total + len(hashtags)

print("Total hashtags:", total)


# ============================================================
# HOW IT WORKS
# ============================================================
# r"#\w+"  = a # and then one or more word characters (letters, digits, _)
# r"@\w+"  = the same idea with an @
# findall() gives back a list, and an empty list [] when nothing is found -
# that is why the third caption prints two empty lists.
# len() counts how many hashtags that caption had, and total adds them up.
