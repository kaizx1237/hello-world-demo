toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizzas!")

pizzas = list(zip(prices, toppings))

print(pizzas)

pizzas.sort()

cheapestPizza = pizzas[0]

priciestPizza = pizzas[6]
three_cheapest = []

for x in range (0, 3):
    three_cheapest.append(pizzas[x])

print(three_cheapest)

num_two_dollar_slices = 0
for x in prices:
    if x == 2:
        num_two_dollar_slices += 1

print(num_two_dollar_slices)