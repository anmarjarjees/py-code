# Open file demo.txt and read the contents
# the demo.txt is stored in the root folder for our project/repo "py-code"

# The first step is to create "stream" object
# To read from a file => open the file:
# Syntax: stream = open(file_name, mode, buffer_size)
stream = open('demo.txt', 'rt')
# quick test:
# print(stream.read()) # read() ==> read all the file contents

print("*** More Examples ***")

# NOTES:
# 1. The mode 'rt' is the default for text file reading => it's optional
# 2. mode "rt" requires the file to be exists, otherwise:
# Error Message: FileNotFoundError: [Errno 2] No such file or directory: 'demo.txt'

"""
Mode List:
r - Read (default)
w - Truncate and write (Write new lines and overwrite the existing contents of the file)
a - Append if file exists (adding more/additional lines to the file)
x - Write, fail if file exists (Write to a file if exists, otherwise throw an error)
+ - Updating (read/write)

t - Text (default) => Text File (basic strings)
b - Binary => Images
"""

# Check if the file is readable (not corrupted)
print('\nIs this file readable? ' + str(stream.readable()))

# reading one or more characters, below reading the first character
print('\nRead one character : ' + stream.read(1)) # H

# reading one or more characters, 
# below reading 9 character depending the cursor position
print('\nRead 10 character : ' + stream.read(9)) # i there! 

# reading one line based on the cursor/pointer position
print('\nRead to end of line : ' + stream.readline())

# reading all the lines based on the cursor/pointer position till the end of the line
print('\nRead all lines to end of file :\n' + str(stream.readlines()) + '\n')

# to reset the file pointer to first position (first character):
stream.seek(0)
print('\nFinally: Read one character: ' + stream.read(1))
# It's Important to close the "stream" to close the file
# to avoid any conflict and free out the resources
stream.close()