import datetime


class Member:
    """Member Class is for accepting the following member info:
    - full_name: The Member Full Name (Mandetory)
    - dob: The Date of Birth YYYY-MM-DD (Mandetory)
    - title: The Job Title (Optional) and it's empty by default
    """

    def __init__(self, full_name, dob, title=""):
        self.name = full_name  # self.name will be the full name
        self.dob = dob  # YYYY-MM-DD
        self.job_title = title

        # Python will split the text based on the space in between the first and the last name
        name_parts = full_name.split(' ')
        # index 0 will have the first name value
        self.first_name = name_parts[0]
        self.last_name = name_parts[1]  # index 1 will have the last name value

    def member_age(self):
        """Return the age of the member in years based on their date of birth"""
        # Link: https://www.w3schools.com/python/python_datetime.apsx
        today = datetime.datetime.now()
        # print(type(today)) # <class 'datetime.datetime'>
        # print(today) # 2023-03-15 11:25:56.493971
        dob_parts = self.dob.split('-')
        # for testing:
        # print(dob_parts) # ['1982', '02', '05']
        # current_year - dob_parts[0]

        # age = today.year-dob_parts[0]
        # 2023 - '1982'
        # TypeError: unsupported operand type(s) for -: 'int' and 'str'

        age = today.year-int(dob_parts[0])
        return age


# Outside our class "Member":
# Creating our objects member1, member2, and member3
member1 = Member("Sally Graysons", "1982-02-05")  # YYYY-MM-DD
member2 = Member("Martin Smith", "1972-12-05")
member3 = Member("Alex Chow", "1975-08-01")

# Now I want to know the age of each member (print them):
print(member1.member_age())

print(member2.member_age())
