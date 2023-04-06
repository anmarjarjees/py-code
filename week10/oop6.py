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


member1 = Member("Martin Smith", "1972-12-05")
print(member1.member_age())  # return the age
