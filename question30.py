# Define a function that can accept two strings as input and print the string with maximum length in console.
# #  If two strings have the same length, then the function should print al l strings line by line.

def printstr(x,y):
    if len(x)> len(y):
        print(x)
    elif len(x) < len(y): 
        print(y)
    else :
        print(x)
        print(y)
    

printstr('mujes','game')