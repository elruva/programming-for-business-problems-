# ============================================================
# 07_make.py - Multi-line joke
# ============================================================
# Build a program from scratch that prints a joke on multiple lines.
# ============================================================

# EXAMPLE OUTPUT:
# Why did the chicken cross the road?
# To get to the other side!

# Write your code below:
print("Why did the chicken cross the road?\nTo get to the other side!")


# ============================================================
# OTHER WAYS TO WRITE THE SAME THING
# All versions below are live, so the joke is printed several times
# when you run this file. That is on purpose - compare the code, not
# the output. Comment out the ones you do not want.
# ============================================================

# Option 1 - two print statements. Each print ends its own line.
print("Why did the chicken cross the road?")
print("To get to the other side!")

# Option 2 - triple quotes. The string can span real lines.
# Careful: spaces before "To get" would also be printed.
print("""Why did the chicken cross the road?
To get to the other side!""")

# Option 3 - store the text in variables first, then print them.
question = "Why did the chicken cross the road?"
answer = "To get to the other side!"
print(question)
print(answer)
