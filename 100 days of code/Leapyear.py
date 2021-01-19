#Leap Year

year = int(input("Enter the Year to checK whether it is Leap/ non Leap year? "))

if year % 4 == 0 :
    if year % 100 != 0 :
        if year % 400 != 0:
            print(f'{year} is a Leap year')
else :
    print(f'{year} is a Non-Leap year')