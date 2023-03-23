
my_course = "Python"

result = my_course * 3

print(result)


# ***************
#  String Methods
# ***************

"""
my first line of comment
my second line of comment
my third line of comment
"""

# Django Framework for Web Application


# We use string methods by using a dot (.) after the string variable,
# followed by the method name and a pair of brackets [like Js, functions and methods end with ( and )].

# objName.method()


# .lower() => lowercase (Review: in JavaScript .toLowerCase())
# .upper() => uppercase (Review: in JavaScript .toUpperCase())
# .capitalize() => change the first letter in the sentence to uppercase
# .title() => making every word starts with uppercase

# NOTE: These methods will NOT change the original string variable

my_string = "HELLO WORLD!"
print(my_string.capitalize())  # Hello world!
print(my_string)  # HELLO WORLD!

my_string_lower = my_string.lower()
# this variable "my_string_lower" will be always in lowercase unless if we change it
print(my_string_lower)

one_more = "NICE WEATHER"
one_more.lower()  # A temporary change only on this line
# just on the next line one_more will return to its original value which is all in Capital
print(one_more)  # NICE WEATHER
# OR:
print(one_more.lower())  # nice weather

test = "python test1"
test.upper()  # => PYTHON TEST1
print(test)

my_string_2 = "hElLo WorLD"
my_string_2_upper = my_string_2.upper()
print(my_string_2_upper)

my_string_3 = "good morning everyone!"
my_string_3_capitalize = my_string_3.capitalize()
print(my_string_3_capitalize)  # capitalize the first letter of the first word
# Output: Good morning everyone!

my_string_4 = "one more time good morning everyone!"
my_string_4_title = my_string_4.title()
print(my_string_4_title)  # capitalize every first letter of each word
# Output: One More Time Good Morning Everyone!

# str.replace("text1","text2") => replace text1 with text2
# if "text1" doesn't exist, no replace will take place
my_paragraph = "Hi there, I like to learn JavaScript, it's very good idea to learn JavaScript if you want to work as a programmer!"
print(my_paragraph)

# replace JavaScript with Python
my_paragraph2 = my_paragraph.replace("JavaScript", "Python")
print(my_paragraph2)
# Output: Hi there, I like to learn Python, it's very good idea to learn Python if you want to work as a programmer!
# replace will NOT change the original string inside the variable "my_paragraph"
print(my_paragraph)

# isalpha() => The .isalpha() string method checks to see if the variable my_string is fully alphabetic
# returns True if all the characters are alphabet letters (a-z)

my_code1 = "abcd123"
my_code1.isalpha()
# False => because not all the characters are letters, we have numbers: 1, 2, 3
print(my_code1.isalpha())  # False

my_code2 = "abcdefg"
print(my_code2.isalpha())  # True => all are letters

my_code2 = "12"
print(my_code2.isalpha())  # False

my_code2 = "90.78"
print(my_code2.isalpha())  # False

# The opposite isdigit() => true of all are numbers


print("the string method join(): ")
print("=====================")
# Python String join() Method
# join() =>	concatenates string
# W3schools.com:
# The join() method takes all items in an "iterable"* and joins them into one string
# A string must be specified as the separator
# Iterable variables/data types => lists, tuples, dictionaries
