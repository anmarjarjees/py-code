instructors = [
    # each object has two properties: name and age (dict: keys => values)
    {'name': 'Alex', 'age': 49},
    {'name': 'Sam', 'age': 47},
    {'name': 'Xing', 'age': 50},
    {'name': 'Martin', 'age': 48}
]

"""
Normal Function:
def sorter(item):
    return item['any_key']

Changed to Lambda Function:   
lambda item: item['name']
"""


# normal to lambda:
def square(number):
    return number*number


lambda number: number*number


# Solution#2:
# instead of creating a whole function just for sorting
# as we saw in solution#1, we can use lambda function:
# with just an inline statement

# calling the "lambda" function to be assigned to the "key"
# lambda parameterName: parameterName['property']
instructors.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(instructors)

print("\n\n")

instructors.sort(key=lambda item: item['age'])
print('-- Age --')
print(instructors)

print("\n\n")

# Sort by length of name (shortest to longest)
# returning the length of the name
# using len() fun in Py = count() fun in PHP
instructors.sort(key=lambda item: len(item['name']))
print('-- Name Length --')
print(instructors)
