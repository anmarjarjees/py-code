""" 
All members (instance variables and methods) in a Python class are "public" by default like in PHP. Any member can be accessed from outside the class environment.

Private Members:
Private members of a class are accessible withing the class only
The most secured modifier
Class members can be private by adding the prefix __ (double underscore)
They cannot be accessed outside the class, doing so will give an AttributeError

Protected Members:
Protected members of a class are accessible from within the class and are also available to its sub-classes.

By "convention", adding the prefix _ (single underscore) to the instance varaible or method. So it will NOT prevent the access!
"""


class Member:
    # Class Attributes:
    # -----------------
    info = "CBC Club's Member"

    # More Examples:
    clubName = "Blue Sky"  # public class field (attribute)
    _clubLocation = 'Toronto'  # protected class field (attribute)
    __clubManager = 'Alex Chow'  # private class field (attribute)

    def __init__(self, full_name="", dob="", title=""):
        # Instance Attribute:
        # -------------------
        # a variable created "within" the constructor function (__init()__),
        # An instance attribute is only accessible from the scope
        # of an object instantiated from the class scope (Specific to object)
        self.name = full_name
        self.dob = dob
        self.job_title = title
        # for fun:
        self.any_thing = "I don't know!"
        # more:
        self.test1 = "Test 1"  # public
        self._test2 = "Test 2"  # protected
        self.__test3 = "Test 3"  # private

        name_parts = full_name.split(' ')
        # for testing:
        # print(name_parts)  # ['Sally', 'Graysons']
        self.first_name = name_parts[0]
        # So below we are just assign the value of the last name into a simple python variable named "last_name"
        # Which can only be accessed within the method body (a local scope variable)

        # last_name = name_parts[1]
        # AttributeError: 'Member' object has no attribute 'last_name'
        self.last_name = name_parts[1]


# Creating our object "member1"
member1 = Member("Alex Chow", "1975-10-22")
print(member1.name)  # Alex Chow
print(member1.dob)  # 1975-10-22
print(member1.info)  # CBC Club's Member

# Let's try if we can change its value:
member1.info = "CP24 Club's Member"
print(member1.info)  # CP24 Club's Member

# print(member1.__clubManager) # it's a private attribute
# AttributeError: 'Member' object has no attribute '__clubManager'

member2 = Member("Sally Graysons", "1982-02-05")


print("Member1 First Name: "+member1.first_name)
print("Member1 Last Name: "+member1.last_name)
