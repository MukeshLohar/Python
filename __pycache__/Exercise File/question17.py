# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500


lines =[]
amount = 0
while True :
    x= input()
    if not x :
        break
    else :
        lines = x.split(' ')

    x = lines[0]
    y = lines[1]

    if x == 'D' :
        amount += int(lines[1])
    elif x == 'W' :
        amount -= int(lines[1])
    else : 
        pass

print(amount)