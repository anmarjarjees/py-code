class Instructor:

    # Constructor
    def __init__(self, name):
        # NOTE: below are calling a property: def name(self)
        self.name = name

    """
    Setting the class field "name" as a "property"
    - adding getter method
    - adding setter method
    """

    @property
    def name(self):
        print("Calling Getter Property:")
        return self.__name
    """
    In PHP
    function getName()
        return $this->name
    """

    @name.setter
    def name(self, value):
        # We can validation for checking the name: not nul, not empty...
        # Example: instructor.name = "Alex"
        print("Calling Setter Property:")
        self.__name = value
    """
    In PHP
    function setName(value)
        $this->name = value
    """


# Using a constructor:
# Instantiate an object from the class "Instructor"
instructor1 = Instructor('Alex')
"""
Calling Setter Property:
"""

# Setting its name:
# Code below => Looks like just updating the "name" field
# But it's calling a function
instructor1.name = 'Martin'
"""
Calling Setter Property:
"""

print(instructor1.name)
"""
Calling Getter Property:
Martin
"""

# The code output:
"""
Calling Setter Property
Calling Setter Property
Calling Getter Property
Martin
"""
