# Here is my "module" (python file created/written by us)
# Modules allow you to store reusable blocks of code, such as functions, in separate files.
# They're referenced by using the import statement.


# ***********************************************************
# Creating a module (Think about the module is like a server)
# so this file is our module "helpers_module".py"
# this file can contain x number of functions/classes/etc...
# ***********************************************************

def display(message="Here is my default message", is_raining=False):
    # This condition will be True if is_raining has the value of "True" OR if it has any value
    if is_raining:
        # if variable => We are just asking if this variable has any value or if it's true Then do if block
        if message:  # This condition will be True if message has the value of "True" OR if it has any other value
            print(message)
        else:  # this else will run if message variable has no value "empty string"
            print('Warning! Take your umbrella')
    # in this simple function, if you don't put else the following print message will always run
    # but with else, this message will be printed if the condition is false
    else:
        print(message)


# Let's create another function:
def course_details(age):
    if age >= 18:
        print("Monday - Room#12 - 6:30 PM")
    else:
        print("Tuesday - Room#22 - 7:30 PM")


def number_total(number_list):
    # using for loop with initial of total
    # number_list => a list that contains numeric values
    # declare a new variable with name "total"
    # has to have an initial value of 0
    total = 0
    # we need to use a loop to go through all the elements in this array "number_list"
    # in JS: for(var i=0; i<=number_list.length; i++) { our code goes here }
    for number in number_list:
        # In JS: total += number_list[i]
        # assume number_list = [45.6, 12.78, 10.89, 23.42]
        # adding 45.6 to my container "total"
        # total=total+number # total = 0 + 45.6
        # Or the short way:
        total += number  # the same as we wrote before: total=total+number

    return total    # at the end of this function: return the final total

# our last function to find/return the average (mean) of a list (array) of numbers:


def number_avg(number_list):
    # finding the total by calling our other function number_total():
    total = number_total(number_list)
    return total/len(number_list)  # in PHP => count($numberList)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


course = "Python"

""" 
class Member() {
        
} 

function calculateTax(price) {

}
"""


def calculate_tax(price):
    pass


class Member():
    pass
