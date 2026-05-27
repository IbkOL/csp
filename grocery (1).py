#IBK

#Init
items = ["Milk", "Eggs", "Bread", "Butter","Cheese"]
prices = [3.49, 2.99, 2.79, 3.99, 4.59]


#functions
def check(item_name):
    for i in range(len(items)):
        if item_name == items[i]:
            print("Item found")
            print(f"Bread found in aisle {i}")
            print(f"item costs", prices[i])

def discount(amount):
    for i in range(len(items)):
        prices[i] = prices[i] * (1-amount)
        prices[i] = round(prices[i], 2)
        print(f"Discount Applied! Now Cost = ", prices[i])
    print(prices)

def max_price(float):
    for i in range(len(items)):
        if prices[i] <= float:
            print(items[i])
            print(prices[i])
    if prices[i] > float:
        print("sorry you can't buy anything with 2 dollars")

def out(item1, item2, item3, item4, item5):
    global cost
    cost = 0
    for i in range(len(items)):
        if item1 == items[i]:
            cost = prices[i] + cost
    for i in range(len(items)):
        if item2 == items[i]:
            cost = prices[i] + cost
    for i in range(len(items)):
        if item3 == items[i]:
            cost = prices[i] + cost
    for i in range(len(items)):
        if item4 == items[i]:
            cost = prices[i] + cost
    for i in range(len(items)):
        if item5 == items[i]:
            cost = prices[i] + cost
    print(f"your total is", cost)


#Main
check()
discount()
max_price()
out()

