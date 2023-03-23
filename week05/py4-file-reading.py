# Reading Data From a File

# The python function:
# open() to open a file

# The python methods:
# readlines() which reads all the lines into a list (this method returns a list)
# readline() which reads one line at a time
# read() which reads the entire file
# seek() which moves to a particular point in a file
# close() which closes the file

# Example:
# the code will open a file "data.txt"
# reads the lines it contains into a variable called "lines"
# The 'r' means that the file is opened as read-only
# open() => Open file and return a stream.


my_file = open('data.txt', 'r')

print(type(my_file))  # <class '_io.TextIOWrapper'>

print('printing the variable "my_file":')
print(my_file)
# <_io.TextIOWrapper name='data.txt' mode='r' encoding='cp1252'>

line = my_file.readline()
print(line)

print("\n")

my_file.seek(0)  # move the curser/pointer to the beginning of the file
# restart from the beginning
line_again = my_file.readline()
print(line_again)

# .readlines() => reads all the lines in our file
all_lines = my_file.readlines()
print(type(all_lines))  # <class 'list'>
print(all_lines)
# ['And this is the second\n', 'Here is the third line\n', 'And here the fourth']

my_file.seek(0)  # reset the file pointer
line_final = my_file.readline()
print("Output:", line_final)


# let's try to use read():
# 1) All of the data will be read into a single string, including the newline characters
# 2) When the string is printed to the console now,
# it just appears as text, not a list of strings
# 3) The newline characters cause the string to be displayed over several lines
my_file.seek(0)  # reset the file pointer first
read_file = my_file.read()

print(read_file)

# close the file:
my_file.close()

# Challenge: Reading Data from a File
# Steps:
# 1. Create a function called get_content that takes one parameter called "file",
# which will be the name of a file that we want to read.

# 2. The get_content function should:
# a. use correct methods shown in our lesson to open the file
# b. read the contents of the file
# c. then close the file
# d. and then return the contents from the function.

# 3. Create a variable "lyrics"
# and assign it the value of the return from calling the function get_content
# with the argument: "lyrics.txt"

# 4. Print the value of the lyrics variable to the terminal
