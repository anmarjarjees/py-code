# if condition

my_variable = False  # true
# if (my_variable) {
#     console.log("It's True!");
# }

if my_variable:
    # In Py we DO HAVE to indent (adding spaces)
    # At least (1 space ) has to be placed before each line of this if block:
    # But notice that:
    # 1. By convention we SHOULD really add one TAB (4 spaces) before each line
    # 2. All the lines inside this if condition MUST have the same number of spaces
    # in this example all have (4 spaces = 1 TAB) which is the Python standard
    print("This condition is True")
print("Here is my second line inside if")
print("Here is my third line inside if")
print("That's it, These are all my lines inside if condition")


# Using if else:
light = 'red'  # We can use ' or " with string values

# Like JS we CANNOT use = comparison, also here in Py We have to use ==
if light == 'green':
    print('You may proceed')
    print('Take your bus')
else:
    print('Please wait here')
    print("You can go when the light is green")


# if we put 20 => "20" but after float(): 20
your_num = float(input("Please input another number: "))

if your_num == 10:
    # Task: output => 10 is equal to 10
    # the first 10 will be the variable "your_num"
    # The 3 different ways to output our text and numeric values as we explained before:
    # pass

    # First Way:
    print(str(your_num) + "is equal to 10")

    # Second Way:
    print(f"{your_num} is not equal to 10")

    # Third Way: similar to printf in Java
    print("%s is not equal to 10" % your_num)

# if (your_num==10) {

# }

last_num = float(input("Please input another number for the last time: "))
# check if number is 5 or more or less
if last_num > 5:
    print(f"{last_num} is greater than 5")
elif last_num < 5:
    print(f"{last_num} is less than 5")
else:
    print(f"{last_num} is equal to 5")

# && => and
# || => or
# ! => not

# declare a variable "avg" with the value of 92.0
avg = 92.0

if avg >= 90 and avg <= 100:
    # this condition will work only if True and True
    print("Excellent")
    print("Well done")

# TRUTH TABLE
# Hint:
# - Thinking of True is 1 and False to be 0
# - Thinking of "and" to be * and "or" to be +
# - The result is either 1 or 0 (no 2 in truth table-maximum value is 1)
#
# TRUE and TRUE => TRUE => 1 * 1 = 1
# TRUE and FALSE => FALSE => 1 * 0 = 0
# FALSE and TRUE => FALSE
# FALSE and FALSE => FALSE

# TRUE or TRUE => TRUE => 1 + 1 = 1
# TRUE or FALSE => TRUE => 1 + 0 = 1

# Example of using "or" logical operator:
# You can apply for "Toronto Public Library-TPL" Card for "FREE"
# if you met at least one of the following condition:
# 3 boolean variables:
live_in_toronto = False
study_in_toronto = False
work_in_toronto = True

if live_in_toronto or study_in_toronto or work_in_toronto:
    # if false or false or true
    print("You can have TPL card for free!")
else:
    print("You need to pay for this card")

# Even / Odd Number Check
# if the remainder of dividing the number by 2 is 0 => even
num = 2
if num % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')
