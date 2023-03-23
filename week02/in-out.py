username = input("Type in your name and press return: ")
# username is a String variable

age = int(input("Please enter your age: "))
# year = 365 days => age * 365

# In JavaScript: we can concatenate a variable of string data type with a variable of numeric data type
# Example in Js console.log("My avg:" + avg) # OK only in JS => My avg: 94
# Because JS will implicitly convert the numeric data type to a string

days = 365*age  # days is an integer variable (numeric)
# using str() function

print("Hello "+username+"! you have been alive for at least " + str(days) + " days.")
# TypeError: can only concatenate str (not "int") to str

# println, printf

# We have assigned a string to variable language and an integer to variable version.
language = "Python"  # str type
version = 3.11  # float type

# We are using Python 3.11
# print("We are using "+language+" "+version)
# TypeError: can only concatenate str (not "float") to str
print("We are using "+language+" "+str(version))

# Formatted string literals are a way to improve the human readability of the output:
print(f'We are using {language} {version}')

# len() is function
print(f"{language} has {len(language)} characters")
# Python has 6 characters
