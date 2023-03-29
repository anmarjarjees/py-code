# Reading from a file:
# ********************
prog_file = open('students.txt', 'rt')

# Using for loop:
# Printing all the students
for line in prog_file:
    print(line)

# Printing all the students who are in the CMPG program only:
""" 
The programs code are listed as the 3rd element in every line 
using the one space as delimiter

So we can use a built-in method/function for the string named "split()" :-) 
This function returns a list of the words in the string, using space as the delimiter string.

IMPORTANT NOTE TO REMEMBER:
After reading the entire file, the cursor will stop at the end of the last line in the file,
we need to move it again to the fist character in index 0 by using seek()
"""

# Move back to the start of the file stream
prog_file .seek(0)

for line in prog_file:
    # line#1 => Alex Chow CMPG
    one_line_arr = line.split()
    # print(one_line_arr) # ['Alex', 'Chow', 'CMPG']
    if (one_line_arr[2]=='CMPG'):
        print(line)


# Writing to a file:
# ******************
# instead of just printing the result in the terminal window, we will write it into a file:

# Creating a new file and let's name it "CMPG.txt"
cmpg_file = open('CMPG.txt', 'wt')

# Optional Step => check if the file is writable or not
# (method) writable() -> bool
print('\nCan I write to this "CMPG.txt" file? ' +
      str(cmpg_file.writable()) + '\n')

# Move back to the start of the file stream
prog_file .seek(0)
for line in prog_file:
    one_line_arr = line.split()
    if (one_line_arr[2]=='CMPG'):
        # print(line) # I don't want to print the line :-(
        cmpg_file.write(line)


# Task: Creating another file to save the CSTN list of students
# Repeat the same logic for creating a file:
cstn_file = open('CSTN.txt', 'wt')

# Move back to the start of the file stream
prog_file.seek(0)

for line in prog_file:
    # split each line based on the spaces
    # end up with an array/list of 3 elements for each line
    line_element_arr = line.split()
    # check the third element if it has the text "CMPG"
    if line_element_arr[2] == 'CSTN':
        cstn_file .write(line)


# IMPORTANT NOTE:
# It's strongly preferred to modify the first loop to have else block for CSTN instead of creating another loop!

# Finally, we should close all the files:
prog_file.close()
cmpg_file.close()
cstn_file.close()

     



