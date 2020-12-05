# "Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3"

#method1
value  = input()

values = [ x for x in value.split(' ')]
letters = 0
digits = 0
others = 0

for each in value :
    if each.isalpha() :
        letters = letters + len(each)
    elif each.isdigit() :
        digits += len(each)
    else :
        others += len(each)

print('Letters : {} , Digits: {} , Others :{}'.format(letters,digits,others))

#method2
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"] )
#-----------------------------