# ============================================================
# 05_modify.py - Countdown Timer
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

number = int(input("Enter a number to count down from: "))


while number >= 0:
    print(number)
    number = number - 1

# ============================================================
# TASKS
# ============================================================
# 1. Fix the code so it stops at 1 (not 0)
# 2. Keep asking for input until the user enters a positive number (greater than 0)
# 3. Print "Blastoff!" at the end
# 4. Show the countdown in a nice format: "3... 2... 1..."

# ============================================================
# Write your improved code below:
# ============================================================



# 1. Fix the code so it stops at 1 (not 0)

number = int(input("Enter a number to count down from: "))

while number > 0:
    print(number)
    number = number - 1

while number <=0:
    print("Error, enter only a positive number: ")
    number = int(input("Enter a number to count down from: "))

print("Blastoff!")
