# ============================================================
# 10_make.py - Word Frequency Counter
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Ask the user for the path of a text file (e.g., "story.txt").
# 2. Read the file. If the file does not exist, print an error
#    message and ask again until a valid path is given.
# 3. Split the text into words (split on whitespace) and clean each
#    word: strip surrounding punctuation (.,;:!?"') and lowercase it.
# 4. Count how often each word appears using a dictionary.
# 5. Print the top 5 most common words with their counts.
# 6. Write the full word-count list (one "word: count" per line,
#    sorted by count descending) to "wordcount.txt".

# EXAMPLE OUTPUT:
# Enter file path: story.txt
# Top 5 words:
#   the: 42
#   and: 31
#   to: 25
#   of: 22
#   a: 18
# Full report written to wordcount.txt

# Hint: create a small story.txt yourself for testing.
# Hint: ".strip(\".,;:!?'\\\"\")" removes leading/trailing punctuation.

# ============================================================
# Write your code below:
# ============================================================

# 1 + 2: keep asking until we can actually open the file
text = ""
while True:
    path = input("Enter file path: ")
    try:
        with open(path) as file:
            text = file.read()
        break
    except FileNotFoundError:
        print("No file with that name - try again.")

# 3 + 4: clean each word and count it
counts = {}
for word in text.split():
    word = word.strip(".,;:!?'\"").lower()
    if word != "":
        counts[word] = counts.get(word, 0) + 1

# Put the counts in a list of [count, word] pairs so we can sort them.
# Sorting goes smallest first, so reverse() gives us the biggest first.
pairs = []
for word in counts:
    pairs.append([counts[word], word])
pairs.sort()
pairs.reverse()

# 5: the top 5
print("Top 5 words:")
for pair in pairs[:5]:
    print(f"  {pair[1]}: {pair[0]}")

# 6: the full report
with open("wordcount.txt", "w") as file:
    for pair in pairs:
        file.write(f"{pair[1]}: {pair[0]}\n")

print("Full report written to wordcount.txt")
