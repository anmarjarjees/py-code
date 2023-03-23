# We are calling our module "my_modules" and using total function
from excel_functions import *

# now need to import from colorama:
# we imported a class named "Fore" 
from colorama import Fore

# Part 1: ask the user to input their numbers:
numbers = input(
    "Please enter your list of numbers as comma separated values (csv): ")


# In PHP explode (" ",$myString);
numbers_list = numbers.split(",")

# The syntax: for any_name in my_list_name
for item in numbers_list:
    print(item)

formula = 0
while (formula != 5):
    print(Fore.RED+" ***** Excel Formulas Game ***** ")
    print(Fore.BLUE+"1: Find the total")
    print(Fore.GREEN+"2: Find the average (the mean)")
    print("3: Find the maximum number")
    print("4: Find the minimum")
    print("5: Exit")

    formula = int(input("Please enter you choice: "))

    result = 0
    if formula == 1:
        # call the total() function
        # In Python, we need to declare/create our functions before calling them
        # in other word, the function block has to be placed before calling it
        # and that's we are importing our functions before starting using them
        result = total(numbers_list)
        print("The total of your numbers is: ", result)
    elif formula == 2:
        # call the average() function
        result = average(numbers_list)
        print("The average of your numbers is: ", result)
    elif formula == 3:
        # call the max function
        print("max")
    elif formula == 4:
        # call the min function
        print("min")
    elif formula == 5:
        # call the min function
        print("Thank you, see you again!")
    else:
        print("Please enter a valid option number next time: 1, 2, 3, or 4")
