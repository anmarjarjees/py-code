from pathlib import Path

# Getting the current working directory object
cwd = Path.cwd()

# Getting the file name:
demo_file = Path.joinpath(cwd, 'demo.txt')

# Notice below we CANNOT use , for concatenating:
print('\nThe demo_file:', demo_file, '\n')
# parent_dir => Drive:\User\Your\Full\Path\demo.txt

# Get only the file name out of the full path:
# using "name" property => returns a file name (str)
# The final path component, if any.
print('\nfile name: ' + demo_file.name)
# Output: file name: demo.txt

# Get the extension
# using "suffix" property => returns the file extension str
# The final component's last suffix, if any.
# This includes the leading period. For example: '.txt'
print('\nfile suffix: ' + demo_file.suffix)

# Get the folder
# property chaining like method chaining => .parent.name
# .parent property (the parent of the path)
# then .name property (The final path component)
print('\nfile folder Name: ' + demo_file.parent.name)  # py-code


# Get the size
# (method) stat() -> stat_result [Statistics Result]
# Return the result of the stat() system call on this path:
# (property) st_size => (stream size) returns the file size (int)
# Notice that the size will be in bytes of a plain file; amount of data waiting on some special files.

# print('\nfile size: ' + str(demo_file.stat().st_size) + '\n')

"""
If the file which is in our example "demo.txt" doesn't exist
We will have this error:
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'Drive:\\User\\Your\\Full\\Path\\python-xtra\\demo.txt'
"""
# let's try it with a real exist file:
data_file = Path.joinpath(cwd, 'data.txt')
print('\nfilename: ' + data_file.name + '\nfile size: ' +
      str(data_file.stat().st_size) + '\n')
# file size: 91
