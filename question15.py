# "Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106"

a = input()


def addition(number) :
    if not a.isnumeric :
        return print("kindly enter a numerice value")
    x = int(a) +int(str(a+a+a)) +int(str(a+a+a+a)) + int(str(a+a)) 
    return print(x)

addition(a)

#method2

a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print (n1+n2+n3+n4)