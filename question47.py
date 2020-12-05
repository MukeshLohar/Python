#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

l = [ x for x in range(1,21) if not x%2]

print(l)