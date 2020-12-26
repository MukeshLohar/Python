# # Please write a program which accepts a string from console and print it in reverse order.
# Example:
# If the following string is given as input to the program:

# rise to vote sir

# Then, the output of the program should be:

# ris etov ot esir

s = [ x for x in input().split(' ')]
s = s[::-1]
y= []
for x in s :
    x = x[::-1]
    
    y.append(x)

print(y)