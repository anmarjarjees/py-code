# Creating a list of objects (three objects):

obj1 = {
    'name': 'Alex',
    'age': 49
}

obj2 = {
    'name': 'Sam',
    'age': 47
}

instructors = [
    {'name': 'Alex', 'age': 49},
    {'name': 'Sam', 'age': 47},
    {'name': 'Xing', 'age': 50},
    {'name': 'Martin', 'age': 48}
]

instructors.sort()
# sort() is not supported for instances of 'dict'

print(instructors)

inst_names = ['Alex', 'Sam', 'Xing', 'Marting']
inst_names.sort()

print(inst_names)
