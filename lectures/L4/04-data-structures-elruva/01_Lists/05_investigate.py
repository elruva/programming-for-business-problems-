# ============================================================
# 05_investigate.py - Name List Menu System
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

names = ["Alex", "Anita", "Patrick", "Atif", "Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
    print(names)
elif choice == 2:
    name = input("Enter the name:\n>")
    names.append(name)
elif choice == 3:
    print("Enter the index of the name")
    index = int(input())
    print(names[index])
else:
    print("Goodbye")

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What would happen if you choose option "3" and entered index "0"?
# Answer: It prints Alex, because indexing starts at 0.

# Q2: What would happen if you choose option "3" and entered index "7"?
# Answer: IndexError: list index out of range - the list only has 5 names.

# Q3: What would happen if you choose option "2" and entered the name "Stuart"?
# Answer: append() puts "Stuart" at the end of the list, but the program then ends without showing it.
