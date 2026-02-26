# Store prices of sold items in tuple
prices = tuple(map(float, input("Enter item prices separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item
print("Cheapest item price:", min(prices))

# c) Costliest item
print("Costliest item price:", max(prices))

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
costliest = max(prices)
count = prices.count(costliest)
print("Number of costliest items sold:", count)