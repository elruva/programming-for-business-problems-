# ============================================================
# 04_modify.py - Compare Three Numbers
# ============================================================
# Starting from the code below, extend it to compare three numbers.
# ============================================================

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

if number1 > number2:
    print("Number 1 is bigger than number 2")
elif number2 > number1:
    print("Number 2 is bigger than number 1")
else:
    print("Both numbers are the same")

# ============================================================
# TASKS
# ============================================================
# 1. Ask the user for a third number.
# 2. Compare it with number1 and number2.
# 3. Print a message describing which number is the largest
#    (or if two/all three are equal).


number3 = int(input("Please enter a thirf number: "))

if number3 == number2 and number3 == number2:
    print("All three numbers are the same")
elif number3 > number2 and number3 > number1:
    print("Number 3 is the largest number")
elif number2 > number1 and number2 > number3:
    print("Number 2 is the largest number")
elif number1 > number2 and number1 >number3:
    print("Number 1 is the largest number")
else:
    print("All the three numbers are the same")

