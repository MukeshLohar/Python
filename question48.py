#Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

l = [ x for x in range(1,21) if not x%2]

print(l)