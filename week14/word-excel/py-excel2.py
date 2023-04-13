# We need to import "Workbook" class for creating a new file
from openpyxl import  Workbook, load_workbook

# Creating a new workbook
wb= Workbook()

# Access the active worksheet
# Always we have one active by default:
sheet = wb.active

# change it's title:
sheet.title = "Students"

# Instead of using the manual way as we did with the first example,
# we can use the .append() method to append a list of cells all at once!
sheet.append(['Name','Program'])

# save the excel file
# wb.save('test2.xlsx')

sheet.append(['Alex Chow','CMPG'])
sheet.append(['Alex White','CSTN'])
sheet.append(['John Doe','CSTN'])
sheet.append(['Jane Smith','CMPG'])

wb.save('test2.xlsx')


"""
Important Note:
Notice that every time, we are initializing a new workbook
that's why we always recreate and add the new data from scratch
"""






