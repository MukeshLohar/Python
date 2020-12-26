#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
#  Then the function needs to print the last 5 elements in the list.

def sqr():
    s = []
    for i in range(1, 21):
        s.append( i ** 2)
    print(s[-5:])

sqr()