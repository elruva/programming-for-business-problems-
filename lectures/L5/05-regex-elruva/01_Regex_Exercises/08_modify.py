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
