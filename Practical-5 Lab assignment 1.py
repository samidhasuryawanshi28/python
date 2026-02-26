# Take series of integers from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(numbers))

# b) Last item
print("Last item in tuple:", numbers[-1])

# c) Tuple in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if 5 is present
if 5 in numbers:
    print("5 is present in the tuple")
else:
    print("5 is not present in the tuple")

# e) Remove first and last items, sort remaining
if len(numbers) > 2:
    new_tuple = tuple(sorted(numbers[1:-1]))
    print("After removing first & last and sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last")