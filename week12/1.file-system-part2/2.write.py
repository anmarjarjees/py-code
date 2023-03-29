# Open output.txt as a text file for writing
# we have to specify 'wt' for Writing Text File as it's not the default mode
stream = open('output.txt', 'wt')
# NOTES:
# 1. mode "wt" will create a new a text file based with the passing name
# 2. if the file is already exists, it will override it

# (method) writable() -> bool
# check if the file is writable or not
print('\nCan I write to this "output.txt" file? ' + str(stream.writable()) + '\n')

# Start writing to the file:
# ***************************
# Task: write "Hello World!" using .write() and .writelines()
stream.write('H')  # Write a single string/character => 'H'
# Notice that the curser/pointer will move to next character which is the space after 'H'

# Adding the rest of the text "ello World!" => passing them as an array of strings
stream.writelines(['ello', ' ', 'world!'])  # Write one or more strings

# Prepare a list/array of names:
names = ['Alex', 'Sam', 'Martin', 'Sarah']

# writing the list of text into our "stream" object
# (method) writelines(__lines: Iterable[str], /) -> None
# writelines() can accept any list object or anything that we can iterate over
# this list object contains elements of string data types
stream.writelines(names)  # will write => AlexSamMartinSarah
stream.write('\n\n')  # Write 2 new lines

# NOTE:
# When iterating through the values of a list, all will be printed without spaces
# we can use .join() string method with literal string '\n'
# to insert a new line between items in the list!
stream.writelines('\n'.join(names))

stream.write('\n\n')  # Write 2 new lines
# Or to add spaces only:
stream.writelines(' '.join(names))

stream.seek(0)
stream.write('We are learning Python') 

# Final step after finishing working with files:
stream.close()  # .close() will flush the stream, save it, and close it
