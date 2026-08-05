# ============================================================
# 05_modify.py - Extract parts of a date using slicing
# ============================================================
# The variable below holds a date in the format "YYYY-MM-DD".
# Use string slicing to print the year, the month, and the day,
# each on its own line.
# ============================================================

date = "2026-04-21"

print(date)

# Modify / extend the code above so the output is:
# 2026
# 04
# 21

print(date[0:4])
print(date[5:7])
print(date[8:10])


# ============================================================
# OTHER WAYS TO WRITE THE SAME THING
# All versions below are live, so the date parts are printed several
# times when you run this file. That is on purpose - compare the code,
# not the output. Comment out the ones you do not want.
# ============================================================

# Option A - store each part in its own variable first.
# Longer, but easier to read and to reuse later.
year = date[0:4]
month = date[5:7]
day = date[8:10]
print(year)
print(month)
print(day)

# Option B - leave out the 0, and leave out the end number.
# [:4] means "from the start" and [8:] means "to the end".
print(date[:4])
print(date[5:7])
print(date[8:])

# Option C - count from the end with negative numbers.
# -5 is the second dash, -2 is the first digit of the day.
print(date[0:4])
print(date[-5:-3])
print(date[-2:])
