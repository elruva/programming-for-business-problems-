# ============================================================
# 05_investigate.py - String Replace Method
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

phone = "123-456-7890"
clean_phone = phone.replace("-", "")
print(clean_phone)

text = "I like cats. Cats are great. CATS!"
new_text = text.replace("cats", "dogs")
print(new_text)

# ============================================================
# QUESTIONS
# ============================================================

# Q1: Why doesn't "CATS" get replaced in the last sentence?
# Answer: replace() matches exactly, and "CATS" and "Cats" are not the same text as "cats".

# Q2: How could you fix this to replace all variations of "cats"?
# Answer: Lowercase the text first, then replace:
print(text.lower().replace("cats", "dogs"))
