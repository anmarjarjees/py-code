# 1: Total
def total(any_list):
    # using for loop to find the total of the numbers
    # any_list => a list that contains numeric values
    # declare a new variable with name "total"
    # has to have an initial value of 0 as this will be the main container
    total = 0
    # we need to use a loop to go through all the elements in this array "number_list"
    # in JS: for(var i=0; i<=number_list.length; i++) { }
    for number in any_list:
        # assume number_list = ["45.6", "12.78", "10.89", "23.42"]
        # adding 45.6 to my container "total"
        # in Python we have two functions to convert string into number: int() and float()
        # the same as we wrote before: total=total+ float(number)
        total += float(number)
        # the end of my loop

    # at the end of this function (outside nd after the loop)
    return total


# 2: Average:
# As a programmer, you have the choice to make this function independent
# By finding the total and the average within the same function
# the other choice, we can make this function using the total function (this function will depend on total functions)
def average(any_list):
    # we are calling our function total() inside the average() function
    # len() as the function to return the length of any list "array" => in JS we used a property "length" array.length
    avg = total(any_list)/len(any_list)
    return avg
    # or using this short way
    # return (total(any_list)/len(any_list))

# Your Task:
# ----------
# 2: Min:
# 3: Max:
