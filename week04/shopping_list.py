

item_number = int(input("How many items did you buy?"))  # 3

# Declare our empty list:
price_list = []

for item in range(item_number):
    # testing:
    print(item)  # => 0, 1, 2
    # print(type(item)) => int
    price = float(input("Enter the price for your current item: "))
    price_list.append(price)


# testing:
print("Price List: ", price_list)

# loop to print all the items

# Finding the total of these items:
total_price = 0
for item in price_list:
    # print("Item Price: ",item)
    total_price += item

print("Your receipt total: %s" % (total_price))
