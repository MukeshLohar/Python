# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the company name of a given email address. Both user names and company names are composed of letters only.


import re
emailAddress = 'mukesh@yahoo.com'
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))