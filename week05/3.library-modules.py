# from the random library => we only need one method (function)
# .randint()

# Using Modules:
# In Python, we call a Python file a "module".
# as developers, we also create modules every time we create our python files.
# We can even import functions, classes, and variables from other modules (python files)
# The syntax: from file_name import required_function

# Example:
# we want to use a built-in function named randint() to generate random integer numbers
# This function inside a module (a python file) named "random"
# the "random" module (Py file) contains "randint()" function

# Case1: you can use this import statement
# importing only randint() function/method from the module random
from random import randint

# using , for more importing more than one function
# using * for importing all the functions
from functions import add1, multiply1

from functions import *

# Or using:
import functions

result1 = add1(4, 5)
print(f"\n4+5 = : {result1}")

result2 = multiply1(4, 5)
print(f"\n4*5 = : {result2}")


# to call "randint" => randint(a: int, b: int)
# Return random integer in range [a, b], including both end points
# printing a random integer value between 1 and 100
print(randint(1, 100))


functions.add1(1, 2)
functions.multiply1(2, 3)
functions.show_content("Alex")
