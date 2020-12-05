# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a consol

# Method 1 --defining a function
L_num = []
x = 1


def factorial(number):
    while number > 0:
        L_num.append(number)
        number -= 1

factorial(8)

for item in L_num:
    x = x * item

print(x)


#method 2
import math

fac = math.factorial(3)
print(fac)


#method3
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


print(fact(7))