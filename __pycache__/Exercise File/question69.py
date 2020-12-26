# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 100

# Then, the output of the program should be:

# 0,35,70

x = int(input())

l = [ str(a) for a in range(0, x + 1) if (a % 5 ==0  and  a % 7 == 0)]

print(','.join(l))