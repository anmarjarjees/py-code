# list
# tuple
# dictionary

fruits = ['apple', 'orange', 'banana', 'pear', 'plum']
# Slicing Lists
print(fruits[0:2])  # ['apple', 'orange']

# Will start from index 0 by default
print(fruits[:2])  # ['apple', 'banana']

# Will start from index 4 and will continue till the rest by default
print(fruits[4:])  # ['plum']

# Tuples: provide us with another means (format) of storing collections of data
# Tuples are also 0 based index
my_tuple = ("Hello", "World")  # it's ( ) not [ ] like a list

# to access any element in the tuple structure we use the [ ]
print(my_tuple[1])  # World

# Working with Dictionary in python (JSON in JS, Associative in PHP)
# key => value
user = {
    "username": "alexchow",
    "first_name": "Alex",
    "last_name": "Chow",
    "email": "alex@idontknow.ca",
    "age": 24,
}

"""
$user = [
    "username" => "alexchow",
    "first_name" => "Alex",
    "last_name" => "Chow",
    "email" => "alex@idontknow.ca",
    "age" => 24,
]
"""

my_book = {
    "title": "All About Python",
    "publisher": "Pearson",
    "author": "Alex Chow",
    "edition": 2,
    "release_year": 2021,
    "is_required": False,
}

print(user.items())

# for in
for item in user:
    print(item)  # => only print the keys (not the values)

for key, value in my_book.items():
    # print(key, value)
    # better format:
    print(f"{key}: {value}")
