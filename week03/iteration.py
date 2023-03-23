# in JS:
# for (let count=1; count<11; count++)
# {
# write the code
# }

# Below is our JS array:
# let sports = ["Basketball", "Football", "Tennis", "Chess", "Swimming", "Running"];

# In Python we use the plain english word "List" to refer to an array variable:
language1 = "HTML"
language2 = "CSS"
language3 = "JavaScript"

languages = ["HTML", "CSS", "JavaScript"]
# In JS:
# for (var i=0; i<languages.length; i++) {
#     console.log(languages[i]);
# }

# looping through a list (array)
# for in
for language in languages:
    print(language)

"""
In PHP:
for $languages as $language {
    print($language)
}
"""

# We can also loop through a string!
my_current_subject = "Python Fundamentals"

# for in
for character in my_current_subject:
    print(character)

# OR:
for character in "Python Fundamentals":
    print(character)

# Formatted string literals are a way to improve the human readability of the output:
print(f'We are using {language3}')

# The range() function:
# we need to loop from min 1 to maximum 10 (from 1 to 10)
for count in range(1, 11):
    print(f"Count number: {count}")

# print the even numbers: 0 to 10
print("Even Numbers: 0 - 10")
for even_number in range(0, 11, 2):  # 0 2 4 6
    # print(even_number)
    print(f"Even number: {even_number}")

# print the odd numbers: 1 to 9
for odd_number in range(1, 10, 2):  # 1 3 5 ...
    print(f"Even number: {odd_number}")


# 255 to be maximum (256-1)
# start 0
# for number in range(256):
#     print(number)

# In JS:
# var count = 1;
# while (count<11) {
#     console.log(count);
#     count++;
# }

count = 1
while (count < 11):
    print(count)
    # in Py: we don't increment/decrement operators count_num++
    # count = count+1
    # the shorthand:
    count += 1

# Example:
play_game = True  # flag variable


while play_game:  # this while loop will stop when play_game value became False
    continue_playing = input(
        "Would you like to continue playing the game? y/n ")
    # Y => y - y => y
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("We will stop the game.")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")


# more examples:
# we can store them in a list, so we have them all in the one place
fruits = ["apple", "banana", "peach", "pear", "plum", "orange", "Lemon"]
print(fruits)  # output: ['apple', 'banana', 'peach', 'pear', 'plum', 'orange']

# or for loop:
for fruit in fruits:
    print(fruit)

# using while with list:

# don't go beyond the maximum index of the list (array):
# error: IndexError: list index out of range
count = 0
# in JS arrayName.length => the length
# in PHP count(arrayName)
# in Python len(arrayName)
while (count < len(fruits)):
    print(fruits[count])  # fruits[0] => apple, fruits[1] = banana
    # in Py: we don't increment/decrement operators count_num++
    # count = count+1
    # the shorthand:
    count += 1
