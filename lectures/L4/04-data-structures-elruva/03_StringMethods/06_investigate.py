# ============================================================
# 06_investigate.py - Chaining String Methods
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

# Processing a list of customer emails
emails = ["  JOHN@MAIL.COM  ", "sara@mail.com", "  Mike@Mail.Com"]

cleaned_emails = []
for email in emails:
    clean = email.strip().lower()
    cleaned_emails.append(clean)

print(cleaned_emails)

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What two string methods are being combined here?
# Answer: strip() removes the spaces and lower() makes everything lowercase.

# Q2: Why is it important to clean email addresses this way?
# Answer: So the same address written differently is stored once and comparisons still work.
