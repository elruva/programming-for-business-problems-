# ============================================================
# 08_modify.py - IP Address Matching
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

import re

ip_addresses = [
    "192.168.1.1",     # valid
    "10.0.0.255",      # valid
    "8.8.8.8",         # valid
    "172.16.254.1",    # valid
    "256.100.50.25",   # invalid (256 is out of range)
    "192.168.1",       # invalid (only three blocks)
    "1.2.3.4.5",       # invalid (five blocks)
    "999.0.0.1",       # invalid (999 is out of range)
]

# Starter pattern - it is far too loose!
reg = re.compile(r"\d.\d.\d.\d")

for ip in ip_addresses:
    print(ip, "->", reg.search(ip))

# ============================================================
# TASK
# ============================================================
# The starter pattern above is far too loose. Improve it so that it matches
# ONLY the valid IPv4 addresses in the list and rejects the invalid ones.
#
# An IPv4 address has the following properties:
# - it consists of exactly four blocks (called octets)
# - the blocks are separated by dots
# - each block is a whole number from 0 to 255
#
# It is up to you to figure out which regex tools you need.

# ============================================================
# Write your improved code below:
# ============================================================

# One block (octet) is a number from 0 to 255, written as four choices:
#   25[0-5]   250 to 255
#   2[0-4]\d  200 to 249
#   1\d\d     100 to 199
#   \d\d?     0 to 99 (one digit, and a second one is optional)
octet = r"(25[0-5]|2[0-4]\d|1\d\d|\d\d?)"

# ^ and $ force the WHOLE string to be the address, so nothing extra can hide
# at the start or the end. {3} asks for exactly three more ".block" parts.
reg = re.compile("^" + octet + r"(\." + octet + "){3}$")

for ip in ip_addresses:
    print(ip, "->", reg.search(ip))


# ============================================================
# OTHER WAYS TO WRITE THE SAME THING
# Uncomment one at a time (remove the #) and run it.
# Remember to comment out the active version above, or the output repeats.
# ============================================================

# Option A - the same pattern written out in one long line, no variable.
# reg = re.compile(r"^(25[0-5]|2[0-4]\d|1\d\d|\d\d?)(\.(25[0-5]|2[0-4]\d|1\d\d|\d\d?)){3}$")

# Option B - print "valid" or "invalid" instead of the match object.
# for ip in ip_addresses:
#     if reg.search(ip):
#         print(ip, "-> valid")
#     else:
#         print(ip, "-> invalid")

# Option C - only checks the shape (four blocks of 1-3 digits), NOT the range.
#            It still lets 256 and 999 through, so it is not enough here.
# reg = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
