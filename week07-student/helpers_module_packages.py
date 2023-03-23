from colorama import Fore, Back
# Markdown language

# Examples from the Colorama page:
# The link for this package: https://pypi.org/project/colorama/
"""
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print('back to normal now')
"""


def display(message="Here is my default message", is_raining=False):
    if is_raining:
        if message:
            print(Fore.RED + message)
        else:
            print(Fore.BLUE+'Warning! Take your umbrella')
    else:
        print(Back.GREEN + message)


def course_details(age):
    if age >= 18:
        print(Fore.GREEN+"Monday - Room#12 - 6:30 PM")
    else:
        print(Fore.YELLOW+"Tuesday - Room#22 - 7:30 PM")


def number_avg(number_list):
    # finding the total by calling our other function number_total():
    # using sum() built-in function to find the total of any list's elements
    total = sum(number_list)
    return total/len(number_list)  # in PHP => count($numberList)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
