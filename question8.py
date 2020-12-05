# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

#method1

values= input('enter the values :')

input_list = [str(x)  for x in values.split(",")]

input_list.sort()
print(','.join(input_list))