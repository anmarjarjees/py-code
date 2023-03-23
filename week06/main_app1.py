# *****************************************************************************
# here is the file where we need to import the module into it:
# If the module is the "server" so think about this file to act as the "client"
# *****************************************************************************


# We have 3 different ways:

# First Way:
# from the module, importing specific function(s)
# ***********************************************
# Syntax: from module_name import function_name

# from helpers_module import display

# You can specify a list of functions using the comma ","
# from helpers_module import display, number_total, number_avg

# Second Way:
# import all (all the functions/code) into the current namespace (file) using the wildcard *:
# from helpers_module import *

# Third way:
# using just the import
# *********************
import helpers_module

# NOTE:
# In the "first" and "second" way:
# ********************************
# we DON'T need to specify the namespace "helpers_module"
# before our functions when we call them
# we can call any function by writing the function name and it's arguments only
# These two ways: will make everything in this module "helpers_module" become globally available

# In the "third" way:
# *******************
# we Do need to specify the namespace "helpers_module"
# >> the "namespace" is the module (python file) name
# >> then dot notation
# >> then function/varaible/class name
# Example: helpers_module.display()

helpers_module.display()


helpers_module.display("It's fine")

# Note to remember :-)
# passing the boolean value "True" => it's raining
# the default value is false => not raining
helpers_module.display("Don't forget to take your umbrella", True)

print(helpers_module.is_even(20))

my_list = [89, 78.67, 90, 78.54, 4, 3]
helpers_module.number_total(my_list)


print(helpers_module.course)
