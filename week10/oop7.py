import datetime


class Member:
    def __init__(self, full_name, dob, title=""):
        self.name = full_name  # self.name will be the full name
        self.dob = dob  # YYYY-MM-DD
        self.job_title = title

        # Python will split the text based on the space in between the first and the last name
        name_parts = full_name.split(' ')
        # index 0 will have the first name value
        self.first_name = name_parts[0]
        self.last_name = name_parts[1]

    def member_age(self):
        today = datetime.datetime.now()

        # pattern: YYYY-MM-DD
        # Slicing String in Python:
        dob_year = int(self.dob[0:4])
        # for testing:
        # print(dob_year)  # for example: 1982
        dob_month = int(self.dob[5:7])
        dob_day = int(self.dob[8:10])

        dob_obj = datetime.datetime(dob_year, dob_month, dob_day)

        age_in_days = today - dob_obj

        age = age_in_days.days/365

        return int(age)

    def print_full_info(self):
        print("\n******************")
        print("Member Information:")
        print("******************")
        # Quick Test for accessing the method "member_age()":
        # print(self.member_age())
        # we can use the f-string to format our output
        print(f"First Name: {self.first_name}")
        # or use the comma:
        print("Last Name: ", self.last_name)
        # or use the concatenation:
        # Notice that we need to add self. before calling any class method
        print("Date of Birth: " + self.dob +
              ". Age: " + str(self.member_age()))
        if self.job_title != "":
            print("Job Title: ", self.job_title)


class Basic_Member(Member):
    # Override the function that we have in the parent(super)class:
    def print_full_info(self):
        # we need to call our function from the superclass:
        Member.print_full_info(self)
        print("Membership Type: Basic")


class Standard_Member(Member):
    def print_full_info(self):
        Member.print_full_info(self)
        print("Membership Type: Standard")


class Premium_Member(Member):
    def print_full_info(self):
        Member.print_full_info(self)
        print("Membership Type: Premium")


# Now let's create our objects:
# Creating our objects "member1, member2, member3"
member1 = Basic_Member("Sally Graysons", "1982-02-05")
member2 = Standard_Member("Alex Chow", "1972-09-23")
member3 = Premium_Member("Martin Smith", "1974-04-03")

member1.print_full_info()
member2.print_full_info()
member3.print_full_info()
