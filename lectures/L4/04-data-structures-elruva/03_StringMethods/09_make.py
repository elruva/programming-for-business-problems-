# ============================================================
# 09_make.py - CSV Line Parser
# ============================================================
# MAKE: Create a program from scratch.
# ============================================================

# REQUIREMENTS:
# 1. Start with a list of "raw CSV lines" (provided below)
# 2. For each line:
#    - Strip whitespace
#    - Split by comma
#    - Clean each field
#    - Store as a dictionary with keys: name, department, salary
# 3. Calculate and print the average salary
# 4. Find and print the employee with the highest salary
# 5. Print all employees in the "Sales" department

# Raw data to process:
raw_lines = [
    "  John Smith , Sales , 55000  ",
    "Sara Jones,Marketing,62000",
    "  Mike Brown , Sales , 48000",
    "Anna Lee,Engineering,75000  ",
    "Tom Wilson , Marketing , 58000"
]

# EXAMPLE OUTPUT:
# Average salary: 59600.00
# Highest paid: Anna Lee (75000)
# Sales department: John Smith, Mike Brown

# ============================================================
# Write your code below:
# ============================================================

employees = []

for line in raw_lines:
    parts = line.strip().split(",")
    employee = {
        "name": parts[0].strip(),
        "department": parts[1].strip(),
        "salary": int(parts[2].strip())
    }
    employees.append(employee)

# Average salary
total = 0
for employee in employees:
    total = total + employee["salary"]
print(f"Average salary: {total / len(employees):.2f}")

# Highest paid employee
best = employees[0]
for employee in employees:
    if employee["salary"] > best["salary"]:
        best = employee
print(f"Highest paid: {best['name']} ({best['salary']})")

# Everyone in Sales
sales = []
for employee in employees:
    if employee["department"] == "Sales":
        sales.append(employee["name"])
print("Sales department: " + ", ".join(sales))
