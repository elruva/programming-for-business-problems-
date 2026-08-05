# ============================================================
# 07_modify.py - Video Game List Manager
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]

# ============================================================
# TASKS
# ============================================================
# Build a small menu that lets the user manage the list of video
# games above. Ask for a choice (1, 2, or 3) and react accordingly:
#
# 1. Option 1 should show all the available video games in the list
# 2. Option 2 should allow the user to enter the name of a video game
#    and add it to the list if it is not already there
# 3. Option 3 should allow the user to enter the index of a game and delete it

# ============================================================
# Write your improved code below:
# ============================================================

# Ask for the choice ONCE and store it, otherwise input() runs again for every if.
choice = input("Enter a choice (1,2,3):")

if choice == "1":
    print(videoGames)
elif choice == "2":
    game = input("Enter the name of the game to add:\n>")
    if game not in videoGames:
        videoGames.append(game)
        print(videoGames)
    else:
        print("Game already in list")
elif choice == "3":
    index = int(input("Enter the index of the game to delete:\n>"))
    if index < len(videoGames):
        print(videoGames.pop(index))
        print(videoGames)
    else:
        print("Invalid index")
else:
    print("Invalid choice")