# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

def sqr():
    s = dict()
    for i in range(1, 21):
        s[i] = i ** 2
        print(s[i])


sqr()