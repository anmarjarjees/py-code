# Py by convention => snake_case => first_name
# Java, JS, C# => camelCase => firstName
# Java, JS, C# => PascalCase => class Student

first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

full_name = first_name+" "+last_name


print("Full is: ", full_name)


num1 = input("enter your first number: ")
# in JS => parseFloat() parseInt()
# in PY => float int
num1 = float(num1)  # convert the string to float

num2 = float(input("enter your second number: "))

# "100"+"200" = 100200

# + - * / %
total = num1 + num2  # 2 + 3 = 5 => 23??

# mul = num1 * num2
# TypeError: can't multiply sequence by non-int of type 'str'


# "2" + "3" = 23

print("Total is: ", total)
print("Multiply is: ", mul)
