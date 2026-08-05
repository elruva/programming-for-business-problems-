# ============================================================
# 10_make.py - Product Code Validator
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

import re

codes = [
    "AB-1234",      # valid
    "XY-0001-A",    # valid (optional suffix)
    "ab-1234",      # invalid (letters must be uppercase)
    "AB-12",        # invalid (needs exactly four digits)
    "ABC-1234",     # invalid (needs exactly two letters)
    "AB-1234-AB",   # invalid (suffix is a single letter)
    "QF-99",        # invalid (needs four digits)
]

# REQUIREMENTS:
# A valid product code looks like this:
#   - exactly TWO uppercase letters
#   - a hyphen
#   - exactly FOUR digits
#   - an OPTIONAL part: a hyphen followed by ONE uppercase letter
# Examples: "AB-1234", "XY-0001-A"
#
# 1. Write a regex pattern (with ^ and $ anchors) that matches this format.
# 2. Loop over the list and print each code followed by "valid" or "invalid".
# 3. Print how many codes are valid in total.

# EXAMPLE OUTPUT:
# AB-1234 -> valid
# XY-0001-A -> valid
# ab-1234 -> invalid
# ...
# Valid codes: 2

# Hint: character set [A-Z], quantifier {n}, and an optional group ( ... )?

# ============================================================
# Write your code below:
# ============================================================
