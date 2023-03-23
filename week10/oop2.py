class Member:
    # In PHP public function __construct() { }
    # In Py public Member() { }
    def __init__(self, full_name, dob):
        # initialize the class variables:
        # In PHP $this->name
        # In Py self.name
        # In Java this.name
        self.name = full_name
        self.dob = dob

    # adding other methods:
    def print_name(self):
        # print(self) # <__main__.Member object at 0x000002630A604FD0>

        # print the value of the "name" field for the object itself:
        print(self.name)

     # Just for more practice:
    def hello(self):
        print("Hello World!")


# We are initializing a new member (an instance of class Member)
member1 = Member("Sally Graysons", "1982-02-05")

# we can test:
print(member1.name)  # Sally Graysons
# AttributeError: 'Member' object has no attribute 'name'
print(member1.dob)  # 1982-02-05
# AttributeError: 'Member' object has no attribute 'dob'

member2 = Member("Kate Willson", "1980-12-15")
print(member2.name)  # Kate Willson
print(member2.dob)  # 1980-12-15

member1.hello()
# TypeError: hello() takes 0 positional arguments but 1 was given

# - yes we can add these two fields to our class
# or we can attach them on the fly to any object (Bad Way!)
# - So below is a kind of mess! we will fix it in the next file
member2.first_name = "Martin"
member2.last_name = "Martinos"
print(member2.first_name)  # Martin
print(member2.last_name)  # Martinos
