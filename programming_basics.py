# NUMBERS
# int only converts string to numbers if there are only numbers in string

# STRINGS
# String is any text that you want to be treated as a text
# If we want to add ' in strings

print("Don't DO that")

# Alternatively

print('she said "I want this"')

# Backslash here tells it to treat the next thing as a character regardless of what it is
print('she said "don\'t put it there"')

# Concatinating strings
print("Hello," + "Nick")
print("h" + "e" + "l" + "l" + "o")
print("This costs " + str(6) + " dollars")
print("This costs " + str(6 + 5) + " dollars")

#splitting strings
print("Hello:Nick".split(":"))
print("Hello:Nick:World".split(":"))
print("My name is " + "Hello:Nick:World".split(":")[1])

#Boolean Operators: True and False
print(5 == 5)
print(5 ==4)

print(5 is 5)
print(5 is not 5)
print(5 is not 6)
print(True is True)
print("True" is True)
print("True" is str(True))

#LISTS []

list_ex = ["MOvies", "lists", "Python"]
print(list_ex)

print("I like " + list_ex[2])

#DICTIONARIES {} : Key value pairs
dict_ex = {"name":"nick", "age":27, "hobby":"code"}
print(dict_ex['name'])
print(dict_ex['age'])
print(dict_ex['hobby'])

#VARIABLES

greeting = "Hello world"
greeting = greeting.split(" ")[0]
print(greeting)
print(greeting + " Someone else")
number = 1
secondnumber = 2
print(number * secondnumber + secondnumber * number)
#to find type of a variable


# BUILT IN FUNCTIONS
print(str(5))
print(str(5.6))
print(str(True))
print(int("5"))
print(float("5.6"))
print(bool("True"))
print(len("Hello"))
print(len(["Hello", "nick", "say", "yes"]))
print(sorted([90,6,4,85,66,73,37,45,3,5,6,8,2,1]))
print(sorted(["N",  "P", "A", "f", "a", "G"]))
print(sorted(["N",  "P", "A", "f", "a", "G", "5"]))
print(sorted(["N",  "P", "A", "f", "a", "G", "5", "5.6", "3.6"]))

#USER DEFINED FUNCTIONS
"""
For class names , first letter of each word is capatilized
for function name , snake case is used, that is seperating each word with underscores
"""

def my_function():
    print("My First statement")
    print("My Second Statement")

my_function()

def my_function_1(str1,str2):
    print(str1)
    print(str2)

my_function_1("This is first argument", "This is my second argument")
my_function_1("Stringy","Hello world")

# DEFAULT ARGUMENTS
def print_something(name,age):
    #string conctatination
    print("My name is " + name + " and my age is " + str(age))

print_something("nick", 27)

def print_something_1(name,age):
    # when comma is used it just says print out these things
    print("My name is",name," and my age is",age)

print_something_1("nick", 27)

"""default values to the arguments, if a function is called without any values
    the default values are used
"""
def print_something_2(name = "someone",age = 27):
    print("My name is",name," and my age is",age)
print_something_2()
print_something_2(age=9) #this is keyword arguments : passing values to variables using their name
print_something_2("nick", 80)

# Infinite Arguments
def print_people(*people):
    # * tells that there is going to be an array of arguments
    for person in people:
        print("This Person is", person)

print_people("Nick", "Dan", "John", "Sam", "Pal")

# Return values from functions
def do_math(num1,num2):
    return num1 + num2

sum1 = do_math(11,44)
print(sum1)

# IF, ELIF, ELSE

check = "yo"
if check == False:
    print("IT IS FALSE")
elif check == "Hamburger":
    print("Oh YUMM")
elif check == "yo":
    print("oh yo")
else:
    print("IT IS ACTUALLY TRUE")

# FOR / WHILE
"""
For loop is good if we want to iterate over an array
While is used for the situations where we want to run a loop till a certail condtion is acheived 
or for the times when we want a certain thing to run only on a certain condition
"""

numbers = [1,2,3,4,5,6,7,8,9,0]
for item in numbers:
    print(item)

run = True
current = 1

while run:
    if current == 100:
        run == False
    else:
        print(current)
        current += 1