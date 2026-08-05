# ============================================================
# 04_modify.py - Flexible Shipping Calculator
# ============================================================
# MODIFY: Improve or extend the code below.
# ============================================================

def calculate_shipping():
    weight = 2.5
    base_cost = 5.00
    cost_per_kg = 1.50
    total = base_cost + weight * cost_per_kg
    print(f"Shipping cost: {total:.2f} EUR")

calculate_shipping()
calculate_shipping()
calculate_shipping()

# ============================================================
# TASKS
# ============================================================
# Right now every call returns the same number - the values are
# hardcoded inside the function. Make it flexible:
#
# 1. Turn weight into a parameter so the caller can pass in any
#    weight: calculate_shipping(weight).
# 2. Add cost_per_kg as a parameter with a DEFAULT value of 1.50.
# 3. Add base_cost as a parameter with a DEFAULT value of 5.00.
# 4. Replace the three identical calls with three DIFFERENT ones:
#    - one positional call passing only the weight
#    - one positional call passing weight and a custom cost_per_kg
#    - one call that uses keyword arguments (e.g. base_cost=10)

# ============================================================
# Write your improved code below:
# ============================================================


def calculate_shipping(weight, base_cost=5, cost_per_kg=1.5, ):
    total = base_cost + weight * cost_per_kg
    print(f"Shipping cost: {total:.2f} EUR")

calculate_shipping(45)
calculate_shipping(54,5)
calculate_shipping(3,base_cost=10)


weight = float(input('Weight:'))
calculate_shipping(weight)

