# ============================================================
# 05_investigate.py - Nested Dictionaries for Sales Data
# ============================================================
# INVESTIGATE: Study the code and answer the questions below.
# ============================================================

quarterly_sales = {
    'Mike': {
        'Q1': 12000,
        'Q2': 15000,
        'Q3': 9000,
        'Q4': 18000
    },
    'Sara': {
        'Q1': 10000,
        'Q2': 12000,
        'Q3': 14000,
        'Q4': 11000
    },
    'Julia': {
        'Q1': 8000,
        'Q2': 9500,
        'Q3': 11000,
        'Q4': 13000
    },
    'John': {
        'Q1': 15000,
        'Q2': 13000,
        'Q3': 16000,
        'Q4': 14000
    }
}

for employee in quarterly_sales:
    total = sum(quarterly_sales[employee].values())
    avg = total / len(quarterly_sales[employee].values())
    print(f'{employee}: Total ${total}, Average ${avg:.2f}')

# ============================================================
# QUESTIONS
# ============================================================

# Q1: How is the data structured in the quarterly_sales dictionary?
# Answer: Each name is a key, and its value is another dictionary of quarter -> sales.

# Q2: What does quarterly_sales[employee].values() return?
# Answer: All four sales numbers for that person, without the quarter names.

# Q3: How would you access Mike's Q3 sales directly?
# Answer: quarterly_sales['Mike']['Q3'] - one key, then the next.
print(quarterly_sales['Mike']['Q3'])
