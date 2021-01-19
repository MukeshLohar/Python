#Write your code below this line 👇
def paint_calc(height,width,cover):
    area = height * width
    total_cans = round((area /cover))
    print(total_cans)






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = 2 #int(input("Height of wall: "))
test_w = 3 #int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇

def prime_checker(number):
    for i in range(2,number):
        if number%i ==0 :
            is_prime=False
    if is_prime :
        print('Prime Number')
    else :
        print('Not a Prime Number')


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



