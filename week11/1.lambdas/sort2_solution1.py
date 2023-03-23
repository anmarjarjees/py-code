instructors = [
    # each object has two properties: name and age (dict: keys => values)
    {'name': 'Alex', 'age': 49},
    {'name': 'Sam', 'age': 47},
    {'name': 'Xing', 'age': 50},
    {'name': 'Martin', 'age': 48}
]


# Solution#1:
# sort() method has a "key" parameter that we can assign to it a function name!
# using the "key" parameter allows:
# to pass in a function to call for each list element before it compares items for sorting
# in other words, we are telling the .sort() method to call the "sorter" function
# to know what value/property to look at when sorting this array

def sorter(item):
    return item['name']


# sort() will sort the list by the key "name" or the key "age"
instructors.sort(key=sorter)

print(instructors)

# more example:
students = [
    {'first_name': 'Alex', 'last_name': 'Chow', 'topic': 'Python', 'section': 202},
    {'first_name': 'Sam', 'last_name': 'Simpson', 'topic': 'Php', 'section': 203},
    {'first_name': 'Martin', 'last_name': 'Smith',
        'topic': 'Python', 'section': 204},
    {'first_name': 'Sarah', 'last_name': 'Grayson', 'topic': 'Java', 'section': 205},
]

# The template:
# list_name.sort(key = function) <==> create our custom function
# function => to tell the sort() method the item to sort: first_name, last_name, topic, or section

print("\n\n Students:")
# element (parameter) that will represent the elements of the array


def sort_by(element):
    # return the element of any key we want: first_name, last_name, topic, or section
    return element['first_name']


students.sort(key=sort_by)
print(students)
