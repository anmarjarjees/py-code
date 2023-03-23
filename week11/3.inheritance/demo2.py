# inheritance:
class Person:

    # Constructor: accepts one parameter => name
    def __init__(self, name):
        # create and instantiate a class field on the fly
        self.name = name

    # Adding a method:
    def say_hello(self):
        print('Hello, ' + self.name)


# The inheritance syntax:
# class "Student" extends class "Person"
# Relationship: Student is a Person
class Student(Person):
    # Constructor: accepts two parameters => name and school
    def __init__(self, name, school, program):
        """
        NOTE:
        We need to set the name, school, program in this constructor
        But "name" parameter is already defined in the parent class "Person"
        so the "name" setting should come from the Person class!

        we use super() to call the parent constructor __init__ with its "name" parameter:
        in other word, the value of the field/property "name" will be set by the Person class
        """
        # In Java: super(name)
        # this.school = school; this.program= program

        # In Py => super().method_name()
        super().__init__(name)
        # the school parameter is specific to this class "Student" NOT the parent "Person"
        # We set it normally:
        self.school = school
        self.program = program

        # Adding another additional functionality to the class "Student":
        # Adding another method beside the inherited one
    def print_school_name(self):
        print('School: ' + self.school)


# Put it on action: Using the derived class "Student"
student = Student('Alex', 'ILAC')
student.say_hello()  # Hello, Alex
student.print_school_name()  # School: ILAC

# Check the main code:
# https://github.com/anmarjarjees/python-extra/tree/main/04.Inheritance
