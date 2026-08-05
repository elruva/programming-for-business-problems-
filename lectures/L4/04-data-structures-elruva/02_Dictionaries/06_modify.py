# ============================================================
# 06_modify.py - Quarterly Sales by Quarter
# ============================================================
# MODIFY: Improve or extend the code below.
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

# Currently calculates per employee - modify to calculate per quarter
for employee in quarterly_sales:
    total = sum(quarterly_sales[employee].values())
    avg = total / len(quarterly_sales[employee].values())
    print(f'{employee}: Total ${total}, Average ${avg:.2f}')


# ============================================================
# TASKS
# ============================================================
# 1. Modify the code to calculate the total sales for each QUARTER instead
#    of each employee
# 2. Output should show Q1, Q2, Q3, Q4 totals across all employees

# ============================================================
# Write your improved code below:
# ============================================================

print()

# Add up each quarter across all employees, using the counting pattern
# from the slides: counts[key] = counts.get(key, 0) + value
quarter_totals = {}
for employee in quarterly_sales:
    for quarter in quarterly_sales[employee]:
        sales = quarterly_sales[employee][quarter]
        quarter_totals[quarter] = quarter_totals.get(quarter, 0) + sales

for quarter in quarter_totals:
    print(f'{quarter}: Total ${quarter_totals[quarter]}')
