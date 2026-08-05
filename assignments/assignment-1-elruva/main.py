# ------------------------------------------------------------
# Task 1: Set up the cart - feel free to change the numbers
# ------------------------------------------------------------

import random

price = 30           # selling price per bagel (kr)
cost_per_bagel = 10  # production cost per baked bagel (kr)
stock = 120          # bagels baked in the morning
buy_chance = 0.35    # chance that a passing customer buys a bagel


# ------------------------------------------------------------
# Task 2: Robust opening input
# ------------------------------------------------------------
def ask_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than 0")
        except ValueError:
            print("That is not a whole number. Please try again")


# ------------------------------------------------------------
# Task 3: Simulate the day
# ------------------------------------------------------------
def sell_bagels(customers, buy_chance, stock):
    sold = 0
    for i in range(customers):
        if sold < stock:
            if random.random() < buy_chance:
                sold = sold + 1
    return sold


# ------------------------------------------------------------
# Task 4: Revenue, costs, and profit
# ------------------------------------------------------------
def daily_profit(bagels_sold, stock):
    revenue = bagels_sold * price
    costs = stock * cost_per_bagel
    return revenue - costs


# ------------------------------------------------------------
# Task 5: Daily report
# ------------------------------------------------------------
def daily_report(bagels_sold, profit):
    left_over = stock - bagels_sold
    revenue = bagels_sold * price
    costs = stock * cost_per_bagel
    print("-------- Daily Report --------")
    print(f"Bagels sold: {bagels_sold}")
    print(f"Bagels left over: {left_over}")
    print(f"Revenue: {revenue} kr")
    print(f"Costs: {costs} kr")
    print(f"Profit: {profit} kr")
    print("------------------------------")


# ------------------------------------------------------------
# Task 6: Find the best batch size
# ------------------------------------------------------------
def average_profit(stock, customers, runs):
    total = 0
    for i in range(runs):
        sold = sell_bagels(customers, buy_chance, stock)
        total = total + daily_profit(sold, stock)
    return total / runs



# Optional 1: rainy days (Q7)
def customers_today(customers):
    # 40% of days are rainy, and then only half as many people pass
    if random.random() < 0.4:
        return int(customers / 2)
    return customers


def average_profit_weather(stock, customers, runs):
    total = 0
    for i in range(runs):
        sold = sell_bagels(customers_today(customers), buy_chance, stock)
        total = total + daily_profit(sold, stock)
    return total / runs



# Optional 2: does another price work better? (Q8)
def average_profit_price(stock, customers, runs, test_price):
    chance = 0.65 - 0.01 * test_price
    total = 0
    for i in range(runs):
        sold = sell_bagels(customers, chance, stock)
        total = total + (sold * test_price - stock * cost_per_bagel)
    return total / runs



# Run one day
customers = ask_positive_int("How many customers pass the cart today?\n> ")

bagels_sold = sell_bagels(customers, buy_chance, stock)
profit = daily_profit(bagels_sold, stock)
daily_report(bagels_sold, profit)



# ------------------------------------------------------------
# Task 6: which batch size is best?
# ------------------------------------------------------------
print()
print("Testing batch sizes from 60 to 160...")

best_stock = 60
best_average = average_profit(60, customers, 200)

for batch in range(65, 165, 5):
    average = average_profit(batch, customers, 200)
    if average > best_average:
        best_average = average
        best_stock = batch

print(f"Best batch size: {best_stock} bagels")
print(f"Average profit: {round(best_average)} kr")

# Does the result make sense?
# Answer: Yes - with 300 customers and a 35% buy chance we expect about 105
# buyers a day, so the best batch size lands close to 105.



# Optional 1: best batch size when it can rain (Q7)
print()
print("Testing batch sizes again, now with rainy days...")

best_stock_rain = 60
best_average_rain = average_profit_weather(60, customers, 200)

for batch in range(65, 165, 5):
    average = average_profit_weather(batch, customers, 200)
    if average > best_average_rain:
        best_average_rain = average
        best_stock_rain = batch

print(f"Best batch size on unpredictable weather: {best_stock_rain} bagels")
print(f"Average profit: {round(best_average_rain)} kr")

# Answer: The best batch size gets smaller, because on rainy days half the
# customers stay home and extra bagels would just be thrown away.



# Optional 2: best price and batch size together (Q8)
print()
print("Testing prices and batch sizes together...")

best_price = 20
best_stock_price = 60
best_average_price = average_profit_price(60, customers, 50, 20)

for test_price in range(20, 65, 5):
    for batch in range(60, 165, 5):
        average = average_profit_price(batch, customers, 50, test_price)
        if average > best_average_price:
            best_average_price = average
            best_price = test_price
            best_stock_price = batch

print(f"Best price: {best_price} kr")
print(f"Best batch size: {best_stock_price} bagels")
print(f"Average profit: {round(best_average_price)} kr")