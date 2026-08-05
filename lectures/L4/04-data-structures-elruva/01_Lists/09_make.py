# ============================================================
# 09_make.py - Random Number List Manager
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Create an empty list
# 2. Wait for user input and perform the following based on the choice:
#    - Press 1: Print the list
#    - Press 2: Ask for a number n and add n random numbers (0-20) to the list
#    - Press 3: Remove all duplicated values from the list
#    - Press 4: Output the number of elements and the average value
#    - Press 5: Stop the program

# EXAMPLE OUTPUT:
# Choice: 2
# How many random numbers? 5
# Added 5 random numbers.
# Choice: 1
# [12, 7, 3, 12, 19]
# Choice: 3
# Duplicates removed.
# Choice: 1
# [12, 7, 3, 19]

# ============================================================
# Write your code below:
# ============================================================

import random

numbers = []

while True:
    print("1: show list  2: add random numbers  3: remove duplicates  4: count and average  5: stop")
    choice = input("Choice: ")

    if choice == "1":
        print(numbers)
    elif choice == "2":
        n = int(input("How many random numbers? "))
        for i in range(n):
            numbers.append(random.randint(0, 20))
        print(f"Added {n} random numbers.")
    elif choice == "3":
        # Keep only the first time each value appears
        unique = []
        for number in numbers:
            if number not in unique:
                unique.append(number)
        numbers = unique
        print("Duplicates removed.")
    elif choice == "4":
        if len(numbers) == 0:
            print("The list is empty.")
        else:
            print(f"{len(numbers)} elements, average {sum(numbers) / len(numbers):.2f}")
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
