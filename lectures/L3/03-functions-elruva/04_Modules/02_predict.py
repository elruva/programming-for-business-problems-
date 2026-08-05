# ============================================================
# 02_predict.py - Modules: Different Import Styles
# ============================================================
# PREDICT: What will this code output?
# Write your prediction as a comment after each print() statement.
# ============================================================

import math
from datetime import datetime

# Using math module
radius = 5
area = math.pi * radius ** 2
print(f"Circle area: {area:.2f}")  # Your prediction: Circle area: 78.54

# Using datetime
now = datetime.now()
print(f"Current time: {now.strftime('%H:%M')}")  # %H - hours and %M - minutes (not months), e.g. Current time: 09:30
print(f"Today is: {now.strftime('%A, %B %d, %Y')}")  # Your prediction: Today is: Tuesday, August 04, 2026

# Different import styles
import random as rnd
print(f"Random number: {rnd.randint(1, 100)}")  # Your prediction: a different number from 1 to 100 each run

# ============================================================
# QUESTIONS
# ============================================================

# Q1: What are three different ways to import modules shown here?
# Answer: import math, from datetime import datetime, and import random as rnd.

# Q2: Why do we use math.pi instead of just pi?
# Answer: Because we imported the whole module, so we write module_name.name to reach it.

# Q3: What does "import random as rnd" do?
# Answer: It imports the random module but lets us write the shorter name rnd.

# ============================================================
# After running, check: Were your predictions correct?
# If not, try to understand why the output was different.
# ============================================================
