# In PHP, JS, Python:
# Weakly (loosely) typed languages
myList = ['HTML', 200, 78.56, True, "CSS"]

fruits = ['apple', 'orange', 'banana', 'pear', 'plum']
# Get an item located in a list
second_item = fruits[1]  # the second item/element

# In JS arrayName.push()
fruits.append('cherries')
# $fruits[] = 'cherries';

num_of_items = int(input("how many items did you buy?"))  # "4" => 4
# if the user puts 4 => 4 items
# ask the user 4 times! to insert the price of each item
# the user will input more than one value (price) for their 4 items

# item#1 price => 5.89
# item#2 price => 2.45
# item#3 price => 8.98
# item#4 price => 3.99

# saving all these item prices into a list (array) => multiple values (prices)

# declare an empty array:
price_list = []
count = 1
while (count <= num_of_items):
    # "5.89" => 5.89
    itemPrice = float(input("Enter the price of your current item: "))
    price_list.append(itemPrice)
    # price_list.append(float(input("Enter the price of your current item: ")))
    count = count+1

print(price_list)
