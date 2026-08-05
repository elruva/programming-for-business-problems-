# ============================================================
# 03_predict.py - Username Registration with Duplicates Check
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

usernames = []

while True:
    username = input("Please enter a username (write 'done' to stop)\n")
    if username == 'done':
        break
    if username in usernames:
        print("Sorry! This username is already taken.")  # Your prediction: Sorry! This username is already taken.
        continue
    usernames.append(username)
    print('Success!')  # Your prediction: Success!

print(usernames)  # Your prediction: the list of names that were accepted, e.g. ['ann', 'bob']

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
