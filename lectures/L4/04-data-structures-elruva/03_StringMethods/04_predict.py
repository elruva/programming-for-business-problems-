# ============================================================
# 04_predict.py - Cleaning Raw Data with String Methods
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

# Simulating messy data from a file
raw_data = "  Smith, John ; London ; 85000  "

# Clean the data
clean_data = raw_data.strip()
parts = clean_data.split(";")

name = parts[0].strip()
city = parts[1].strip()
salary = int(parts[2].strip())

print(f"Name: {name}")  # Your prediction: Name: Smith, John
print(f"City: {city}")  # Your prediction: City: London
print(f"Salary: {salary}")  # Your prediction: Salary: 85000

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
