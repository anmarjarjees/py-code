# Open manage.txt file to write text
stream = open('manage.txt', 'wt')

# Write the word 'demo' to the file stream
# not writing in the actual file
stream.write('demo!')

# Move back to the start of the file stream
stream.seek(0)

# write the word 'nice' to the file stream
# this will overwrite'demo'
stream.write('nice')

# Flush the file stream contents to the file buffer
"""
flush(): 
Takes the content of the file stream 
and write it to the actual file. 

If any one is opening the file can see the changes immediately in memory
But this doesn't mean that the file is saved into a disk by the OS

Notice that there is no need for flush() if using .close()
And we have to close the file when we are done with them
So it can be opened next time without issues: file is already open
"""
stream.flush()

# .close() will do the two actions: flush and close
# Flush the file stream and close the file
stream.close()