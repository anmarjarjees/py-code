# In JS:
# function printMessage() {
#     console.log("Hello World!");
# }

# In PHP:
# function printMessage() {
#     echo("Hello World!");
# }

# 1. Create our function
# Notice the use of snake_case in py language:
def print_message():
    print("Hello World!")


# 2. Call the function
print_message()  # Hello world!
print_message()

# name is a parameter for this function (the variable to used inside the function)
# This function is expecting to have a value for the name parameter


def show_content(name):
    # the value of the "name" are being used in this print statement
    print(f"Hello {name}!")


# we can set a default value for "age" parameter in case if we didn't pass any value to the function
# this called an optional parameter
# Optional parameters will allow us to provide values to a function with some value
# in case they are not provided when the function is invoked

def get_user_age(age=15):
    # Docstring:
    """ 
    get_user_age:
    - accepts one argument (the user's age)
    - prints the classroom number
    """
    if age >= 18:
        print("Go to classroom#18")
    else:
        print("Go to classroom#12")


# saving our time by hard coding the age value (instead of input to ask the user)
your_age = 20
get_user_age(your_age)  # Go to classroom#18

# below we are not passing any value, the age will be equal to 10 (by default)
get_user_age()  # Go to classroom#12


def get_user_input(prompt):
    # The return statement (exactly like JS):
    # - returns the result of the function and is the point where the code stops running
    # - statements after a return statement are not executed
    # - can only be used within a function
    # NOTE: if no expression is included in the return statement, then "None" is returned
    return input(prompt)


# 1. name and age are the first two function calls to run sequentially (when we run our app)
name = get_user_input("Input your name:")
age = int(get_user_input("Input your age:"))

print('\n name: ' + name)
print('\n age: ' + str(age))
print(f'\nage: {age}')

# lambda:
# There is another type of function in "Python" known as "Lambda":
# - a small anonymous function (no name just the keyword "lambda").
# - can take any number of arguments but only has one expression
# W3schools: https://www.w3schools.com/python/python_lambda.asp

# Example:

# Here is the normal function of just adding two numbers


def add1(a, b):
    return a + b


# Writing the same function using lambda:
def add2(a, b): return a+b
# As you can see the function has no name (hence anonymous) so we have assigned it to the variable add2
# The pattern: "lambda" the list of the parameters with commas : one expression (one statement)


"""
def add2(a, b):
    return a + b
"""


def multiply1(a, b): return a * b


# Or using lambda
def multiply2(a, b): return a*b
