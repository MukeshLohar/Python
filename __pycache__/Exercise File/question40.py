#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

def sqr():
    s = []
    for i in range(1, 21):
        s.append( i ** 2)
    print(tuple(s))

sqr()
