# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address.
#  Both user names and company names are composed of letters only.


email = "yahooo@google.com"

result = []

def gettingvalur(k):
    i=0
    j=0
    for x in k:
        if x == "@":
            i += 1
        elif x == "." :
            j += 1
    return (i,j)


print(email)


import re
emailAddress = "yahooo@google.com"
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))
