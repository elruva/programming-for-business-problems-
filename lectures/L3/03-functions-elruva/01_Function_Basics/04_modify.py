# ============================================================
# 04_modify.py - Greet Customers with Functions
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

print("--- Customer 1 ---")
print("Welcome to the cafe!")
print("Please take a seat.")
print("Enjoy your meal!")

print("--- Customer 2 ---")
print("Welcome to the cafe!")
print("Please take a seat.")
print("Enjoy your meal!")

print("--- Customer 3 ---")
print("Welcome to the cafe!")
print("Please take a seat.")
print("Enjoy your meal!")

# ============================================================
# TASKS
# ============================================================
# 1. Define a function called welcome_customer() that prints the
#    three welcome lines (Welcome / Please take a seat / Enjoy).
# 2. Replace the duplicated welcome lines by calling the function.
# 3. Define a second function say_goodbye() that prints
#    "Have a great day!" and call it after each customer.

# ============================================================
# Write your improved code below:
# ============================================================

#1 

print("--- Customer 1 ---")
def welcome_customer():
    print("Welcome to the cafe!")
    print("Please take a seat.")
    print("Enjoy your meal!")

welcome_customer()


print("--- Customer 2 ---")
def welcome_customer():
    print("Welcome to the cafe!")
    print("Please take a seat.")
    print("Enjoy your meal!")

welcome_customer()


print("--- Customer 3 ---")
def welcome_customer():
    print("Welcome to the cafe!")
    print("Please take a seat.")
    print("Enjoy your meal!")

welcome_customer()



#3 

print("--- Customer 1 ---")
def welcome_customer():
    print("Welcome to the cafe!")
    print("Please take a seat.")
    print("Enjoy your meal!")
    say_goodbye ()


def say_goodbye():
    print ("Have a great day!")

welcome_customer()


print("--- Customer 2 ---")
def welcome_customer():
    print("Welcome to the cafe!")
    print("Please take a seat.")
    print("Enjoy your meal!")
    say_goodbye ()


def say_goodbye():
    print ("Have a great day!")

welcome_customer()


print("--- Customer 3 ---")
def welcome_customer():
    print("Welcome to the cafe!")
    print("Please take a seat.")
    print("Enjoy your meal!")
    say_goodbye ()


def say_goodbye():
    print ("Have a great day!")

welcome_customer()


#loop for the customers 
for i in range (1,4):
    print ( f'-- Customer {i} --')
    welcome_customer()