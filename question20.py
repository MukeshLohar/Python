# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


def arg_seven(x):
    x = int(x)
    for a in range(1, x):
        if a % 7 == 0:
            yield a
        else:
            pass
        # print("{} is not divisible by 7".format(a))


for a in arg_seven(123):
    print(a)
