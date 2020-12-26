# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].


x= [5,6,77,45,22,12,24]
l = [ l for l in x if int(l)%2  ]

print(l)