# ============================================================
# 01_predict.py - List Basics and Modification
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

Sentence =["Always", "look", "on", "the", "bright", "side", "of"]
print(Sentence)  # Your prediction: ['Always', 'look', 'on', 'the', 'bright', 'side', 'of']
print(Sentence[1])  # Your prediction: look
Sentence.append("life")
Sentence[4] = "sunny"
print(Sentence[4])  # Your prediction: sunny
print(Sentence[0] + " " + Sentence[3])  # Your prediction: Always the
print(Sentence)  # Your prediction: ['Always', 'look', 'on', 'the', 'sunny', 'side', 'of', 'life']
print(" ".join(Sentence))

for i in Sentence:
    print(i, end=" ")

output = " "
for word in Sentence:
    output += word + " "

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
