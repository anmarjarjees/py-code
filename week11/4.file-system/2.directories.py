# Navigate between different directories:
from pathlib import Path
current_dir = Path.cwd()

# current_dir => Drive:\User\Your\Full\Path\py-code

# Get the parent directory
# Using the property "parent" of the Path.cwd() object "current_dir"
parent_dir = current_dir.parent


# Check whether this path is a directory or not:
# Using the method .is_dir() => bool
print('\n----- Directory Check -----')
print('\nIs this "current_dir" a directory? ' + str(current_dir.is_dir()))
print('\nIs this "parent_dir" a directory? ' + str(parent_dir.is_dir()))


# Whether this path is a regular file:
print('\n\n----- File Check -----')
print('\nIs this "current_dir" a file? ' + str(current_dir.is_file()))


# List child directories by using .iterdir() method
# (method) iterdir() -> Generator[Path, None, None]
# Iterate over the files in this directory.
print('\n----- Parent directory Contents-----')
for child in parent_dir.iterdir():
    # display/print only the directories (except the files):
    if child.is_dir():
        print(child)


print('\n----- Current directory Contents-----')
for child in current_dir.iterdir():
    if child.is_dir():
        print(child)
