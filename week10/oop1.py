class Member:
    pass


member1 = Member()

print(type(member1))

print(type("ABC"))

print(member1)

member1.first_name = "Alex"
member1.last_name = "Chow"
# our Class "Member" is empty we can add anything we want:
member1.age = 47
member1.gender = "m"

print(member1.first_name)  # Alex
print(member1.last_name)  # Chow
print(member1.age)  # 47
print(member1.gender)  # m

member2 = Member()
member2.first_name = "Sam"
member2.last_name = "Simpsons"

# We can attach any field to an object with any data type:
member2.job_title = "Teacher"

member2.favourite_singer = "Frank Sinatra"
# object_name.any_field = any value
