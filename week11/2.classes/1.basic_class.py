# Quick Recap:
class Instructor:
    """ 
    Starting with a constructor __init__ 
    for creating an instance/object of this class => constructing an object

    two underscores init two underscores

    The first/mandatory parameter in any function/method inside a class is "self"
    which is similar to the keyword "this" in other programming languages.

    self will give us the access to the current instance of an object
    after the "self" we can start listing any other additional parameter(s) that we need 
    """
    # in PHP => function __construct()

 # This constructor for setting the name
    def __init__(self, name):
        self.name = name

    # Adding other methods to the object:
    # notice that every method must have the parameter "self"
    # method:
    def say_hello(self):
        # Using "self." to access all the class fields
        # calling the class field self.name
        print('Hello, ' + self.name)


# Using a constructor:
# Instantiate an instance/object from the class "Instructor"
instructor1 = Instructor('Alex')

# Accessing the class method "say_hello()"
instructor1.say_hello()
