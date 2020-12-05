# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
#method1
passwords = [ x for x in input().split(',')]
item =[]
abc = 'asdsad'

def len_check(pd):
    if len(pd) <= 12 and len(pd) >= 6 :
        print("password length is correct {}".format(len(pd)))
        return True
    else :
        print("password length is wrong {}".format(len(pd)))
        False

def checkupper(pd) :
    for i in pd:
        if i.isupper() :
            print('{} contains upper letter'.format(pd))
            return True
        else :
            print('{} does not contains upper letter'.format(pd))
            

def checklower(pd) :
    for i in pd:
        if i.islower() :
            print('{} contains lower letter'.format(pd))
            return True
        else :
            print('{} doesnot contains lower letter'.format(pd))
            

def checknum(pd) :
    for i in pd:
        if i.isdigit() :
            print('{} contains numbers'.format(pd))
            return True
        else :
            print('{} doesnot contains numbers'.format(pd))
            

def checkchar(pd) :
    for i in pd:
        if i == '$' or i == '@' or i == '#' :
            print('{} contains chars'.format(pd))
            return True
        else :
            print('{} doesnot contains chars'.format(pd))

for psd in passwords:
    if ( len_check(psd) and checknum(psd) and checkupper(psd) and checklower (psd) and checkchar(psd) ) :
        item.append(psd)
    else:
        print('{} did  not met tht criteria'.format(psd))


    
print(','.join(item))

#method2

import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print (",".join(value))