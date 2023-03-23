class Member:
    # We will use this symbol """ (three double quotes) which is called a "Docstring"
    """  
        Member Class is for accepting the following member info:
        - full_name: The Member Full Name (Mandetory)
        - dob: The Date of Birth YYYY-MM-DD (Mandetory)
        - title: The Job Title (Optional) and it's empty by default
    """

    def __init__(self, full_name, dob, title=""):
        # again: self.name and self.dob are just a variable for our class
        # any variable we create inside a class can be called "Field"
        self.name = full_name  # self.name will be the full name
        self.dob = dob  # YYYY-MM-DD
        self.job_title = title

        # Python will split the text based on the space in between the first and the last name
        name_parts = full_name.split(' ')
        # index 0 will have the first name value
        self.first_name = name_parts[0]
        # Below we fixed the error by adding self.
        self.last_name = name_parts[1]  # index 1 will have the last name value


# Creating our object "member1" which is an instance of the class "Member"
member1 = Member("Sally Graysons", "1982-02-05")

help(Member)
