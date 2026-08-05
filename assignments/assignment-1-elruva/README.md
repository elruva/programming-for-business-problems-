# Bonus Assignment 1: Street Bagel Cart

## Scenario
You are helping a friend who runs a small bagel cart near the harbour. Every morning your friend bakes a batch of fresh bagels; whatever is not sold has to be thrown away in the evening. Baking too few bagels means missing out on sales — baking too many means throwing money away. On a typical busy day, **about 300 customers** pass the cart. Your program will simulate one day of business and then help your friend answer the big question: **how many bagels should be baked each morning?**

You only need the concepts from Sessions 1–3 (variables, input/output, math, flow control, and functions). No lists or other data structures are required.

## Tasks:

### 1. Set Up the Cart
- Create variables for the business:
  - `price`: selling price per bagel, 30 kr.
  - `cost_per_bagel`: production cost per baked bagel, 10 kr (paid for **every** baked bagel, sold or not).
  - `stock`: how many bagels are baked in the morning (start with 120).
  - `buy_chance`: the probability that a single passing customer buys a bagel (start with `0.35`).

### 2. Robust Opening Input
- Create a function `ask_positive_int(prompt)`:
  - Ask the user for input using the given prompt.
  - If the input is not a whole number, or not greater than 0, print a helpful message and ask again.
  - Use a `while` loop together with `try`/`except` so the program never crashes on bad input.
  - Use this function to ask how many customers will pass the cart today. Use **300** (the typical busy day) as your answer for the rest of the assignment.

### 3. Simulate the Day
- Create a function `sell_bagels(customers, buy_chance, stock)`:
  - Simulate every customer walking past the cart (use a `for` loop).
  - Each customer buys a bagel with probability `buy_chance` (hint: `random.random() < buy_chance`).
  - Bagels can only be sold while there are some left — never sell more than `stock`.
  - The function should return the number of bagels sold.

### 4. Revenue, Costs, and Profit
- Create a function `daily_profit(bagels_sold, stock)` that returns the profit of the day:
  - Revenue: bagels sold times the price.
  - Costs: **all baked bagels** times `cost_per_bagel` (unsold bagels are thrown away!).
  - Profit: revenue minus costs.

### 5. Daily Report
- Create a function `daily_report` that receives the bagels sold and the profit.
- Print a nicely formatted summary of the day using f-strings: bagels sold, bagels left over, revenue, costs, and profit in kr.

### 6. Find the Best Batch Size
- The result changes every time you run the program, because the customers behave randomly. To compare batch sizes fairly, write a function `average_profit(stock, customers, runs)` that simulates many days (e.g. 200) with the same batch size and returns the average profit.
- Then try every batch size from 60 to 160 in steps of 5 (use a loop!) and print the batch size with the highest average profit. Use the 300 customers of a typical busy day for this analysis.
- Does the result make sense given the expected number of buyers on such a day?

### 7. Optional 1 (If you want to practice some more)
Aarhus weather is unpredictable: on a rainy day (40% of days) only half as many customers pass the cart. Extend your simulation so that each day is randomly rainy or sunny, and find out how the best batch size changes.

### 8. Optional 2 (If you want to practice even more)
Your friend also wonders about the price. Suppose the buy chance depends on the price: `buy_chance = 0.65 - 0.01 * price` (so at 30 kr the chance is 0.35, at 50 kr only 0.15). Which combination of price and batch size gives the highest average profit? (Hint: you will need one loop inside another.)

## Example Code Structure
### Set Up the Cart

```python
import random

price = 30           # selling price per bagel (kr)
cost_per_bagel = 10  # production cost per baked bagel (kr)
stock = 120          # bagels baked in the morning
buy_chance = 0.35    # chance that a passing customer buys a bagel
```

### Example Report (with 300 customers)

```
-------- Daily Report --------
Bagels sold: 103
Bagels left over: 17
Revenue: 3090 kr
Costs: 1200 kr
Profit: 1890 kr
------------------------------
```
