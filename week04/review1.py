# review.py

# Python Data Types:
# ******************
# The most basic data types in computing are:
# - Boolean (bool) which has two built-in values of "True" or "False"
# - Text has the type of string (str)
# - There are several numeric types such as integer (int), float and complex numbers
# numbers: int and float
# int => whole number (no decimal points)
# float => decimal numbers (fractions)

my_str = "abc"
is_valid = True
average = 78.54
age = 59

# In JavaScript, we used typeof() => return the data type of the variable
# in Py => type() => return the data type of the variable
# Object <==> Class
print(type(my_str))
print(type(is_valid))
print(type(average))
print(type(age))
# <class 'str'>
# <class 'bool'>
# <class 'float'>
# <class 'int'>

# PEDMAS
print(4 / 2)  # output 2.0

# Exponent:
# Exponent means to the power of.
# the result of 2 to the power 3
# find: 2 * 2 * 2
# in Py: 2**3 => 2 to the power of 3 => 2 * 2 * 2
print(2 ** 3)  # 2 * 2 * 2 => output is 8

my_complex_number = 7.777777777
# in PHP round() = in Py:
print(round(my_complex_number, 2))


# -=
# *=
# /=
# **=
# %=
# //=

# Examples:
variable_one = "hello "
variable_two = "world"

variable_one += variable_two
print(variable_one)
print(variable_two)

x = 2
x **= 3

print(x)  # 8

# Strings:
# To escape any character we can use the \
# The escape character is simply a backslash (\)
# Single Quote \'
# Double Quote \"
print("Martin's car is Honda")
print('Martin\'s car is Honda')
print("I like to learn \"Python\"")

# New Line \n
# TAB \t
# Carriage Return \r
# Carriage return \r is often interpreted by the operating system in the same way,

print("Martin's \n car is Honda")
print("Martin's \t car is Honda")
print("Martin's \r car is Honda")


# String Converting:
# Ask the user to input his/her age:
age = input("Please enter your age: ")  # 24 => "24"

# The three mainly used converting functions:
# *******************************************
# int() => converting a float or string to an int
# float() => converting an int or string to a float
# str() => converting an int or float to a string

print("The age is " + age)

exam1 = 80
exam2 = 92
print("Exam1: " + str(exam1) + ", Exam2: " + str(exam2))
print(f"Exam1: {exam1}, Exam2: {exam2}")
print("Exam1: %s, Exam2: %s" % (exam1, exam2))

# Loops:

# In PHP
"""
for ($i=1; $i<11; $i++) {
    echo "<br> $i";
}
"""

# in Py
for count in range(1, 11):
    print(f"Count number: {count}")

    print(" * ")


# print(item, end=" ")
# Link: https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
for even_number in range(0, 11, 2):
    print(f"Even number (for loop3): {even_number}", end=" ")

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]

print(f"The second fruit is : {fruits[1]}")

# Task: Print all the fruits till we reach the "peach" fruit
# We need to break/STOP our loop (Don't print) when the value is "peach"

counter = 0
while counter < len(fruits):
    # You want to break (stop) the loop when we reach the element named "peach"
    if fruits[counter] == "peach":
        break

    print(fruits[counter])
    counter += 1  # In python we don't counter++ as we used to have in JS

# Let's do it using for loop:
# using the break with for loop
# remember that fruit is just a variable that will represent each element in fruits list
for fruit in fruits:
    if fruit == "peach":
        break
    print(fruit)

numbers = [10, 20, 30, 40, 50]
# Task: create new array named double_numbers = [100,400,900,....]

double_numbers = []
for number in numbers:
    double_numbers.append(number ** 2)

print("double_numbers: ", double_numbers)
# double_numbers:  [100, 400, 900, 1600, 2500]

# Modify the same list "numbers"
for index in range(5):
    numbers[index] = numbers[index]**2

# Data Structures:
