#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
s=(1,2,3,4,5,6,7,8,9,10)
l =[x for x in s if not x %2 ]
print(tuple(l))