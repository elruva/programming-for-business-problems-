# ============================================================
# 03_investigate.py - Parameters: Default and Keyword Arguments
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

def greet(name, msg="Good morning!"):
    print(f'Hi {name}, {msg}')

greet("Hans")
greet("Hans", "How are you?")
greet("Good afternoon", "Hans")  
greet("How are you?")          
greet(msg="Good afternoon", name="Hans")
greet(name="Hans")
# greet(msg="Good afternoon")    # Uncomment this - what happens?

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What are the outputs of each function call?
# Answer: Hi Hans, Good morning! / Hi Hans, How are you? / Hi Good afternoon, Hans /
#         Hi How are you?, Good morning! / Hi Hans, Good afternoon / Hi Hans, Good morning!

# Q2: Which parameter has a default value? How can you tell?
# Answer: msg - it has ="Good morning!" written after it in the definition.

# Q3: Why does greet("Good afternoon", "Hans") produce unexpected output?
# Answer: Arguments are matched by position, so "Good afternoon" lands in name and "Hans" in msg.

# Q4: What's the difference between positional and keyword arguments?
# Answer: Positional ones are matched by their order, keyword ones by the name you write.

# The commented-out call greet(msg="Good afternoon") gives:
# TypeError: greet() missing 1 required positional argument: 'name'
