# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters
#method1
class getString :

    def __init__(self):
        self.value =""

    def get_string(self):
        self.value = input()

    def print_upper(self):
        print(self.value.upper())


x = getString()
x.get_string()
x.print_upper()

#method 2

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()