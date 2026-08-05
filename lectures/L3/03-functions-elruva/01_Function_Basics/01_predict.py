# ============================================================
# 01_predict.py - Function Basics: Calling Functions
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

def say_hi():
    print("Hello there!")  # Your prediction: Hello there! (printed second)

def offer_drink():
    '''Asks if the guest wants a drink'''
    print("Would you care for a spot of tea?")  # Your prediction: Would you care for a spot of tea? (printed first)

def offer_food():
    print("Biscuit?")  # Your prediction: Biscuit? (printed third)

def say_bye():
    print("See you later")  # Your prediction: nothing, this function is never called

offer_drink()
say_hi()
offer_food()

# ============================================================
# QUESTIONS
# ============================================================

# Q1: Why does say_bye() never get called?
# Answer: It is only defined, never called - defining a function does not run it.

# Q2: In what order do the functions execute?
# Answer: offer_drink(), then say_hi(), then offer_food() - the order they are called in.

# Q3: What happens if you call say_hi() before defining it?
# Answer: Python stops with NameError, because the name does not exist yet.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
