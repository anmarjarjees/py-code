# In Python, we used to use the os
# OLD-FASHIONED WAY, We will use the new way
# import the os library:
import os


# using the get current working directory function getcwd()
# to find the directory in which the python file is located.
print(os.getcwd())

# We can also list the files or directories listdir() within a directory.
print(os.listdir)  # <built-in function listdir>

print(os.listdir())

# Task: check the list of folders/files in week04
# The path: Drive:\User\your-full-path\Py-Code\week04
# the relative path:week04
print('\n\nWeek04 Contents: ', os.listdir('week04'))
# Week04 Contents:  ['review1.py', 'shopping_list.py']
# read more: https://docs.python.org/3/library/os.html

# os.path() method allows you to dynamically create path names
# so you can connect to files on the operating system
# and save files where you intend to.

# This is how you would join two paths in your code:
print('Our fictional path: ', os.path.join('/home/runner/', 'os'))
