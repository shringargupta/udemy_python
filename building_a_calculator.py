import re

print("Our magical calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run # to access a global variable
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, human")
        run = False
    else:
        equation = re.sub('[a-zA-z:,;" "()]', '', equation)
        if previous == 0:
            previous = eval(equation) #eval can be dangerous as it can evaluate python code as well
        else:
            previous = eval(str(previous) + equation)
while run:
    performMath()