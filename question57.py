# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# john

#method1
email = "yahooo@google.com"

result = []
def gettingvalur(x):

    for i in x:
        if not i == "@":
            yield i
               
        elif i == "@" :
            break

        

for x in gettingvalur(email) :
    result.append(x)

print(''.join(result))

#method2
import re
emailAddress = input()
pat2 = '(\w+)@((\w+\.)+(com))'
r2 = re.match(pat2,emailAddress)
print (r2.group(1))
