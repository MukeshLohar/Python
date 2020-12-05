# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

#method1
lines =[]

while True :
    x= input()
    if x :
        lines.append(x.upper())
    else :
        break

for sen in lines :
    print(sen)