# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

def oddeven(x) :
    x = int(x)
    if not x%2 :
        print("It is even number")
    else :
        print("it is odd number")


oddeven(234)