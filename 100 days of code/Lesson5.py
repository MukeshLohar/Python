# 🚨 Don't change the code below 👇
student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
no_of_pp = 0
for n in range(0, len(student_heights) ):
  student_heights[n] = int(student_heights[n])
    
for height in student_heights:
    total_height += height
    no_of_pp += 1
# 🚨 Don't change the code above 👆
print(round(total_height/no_of_pp,2))
#Write your code below this row 👇 



# 🚨 Don't change the code below 👇
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# 🚨 Don't change the code above 👆
max_mark = 0
for mark in student_scores :
    if mark > max_mark:
        max_mark = mark

print(max_mark)
#Write your code below this row 👇



#Write your code below this row 👇

total_even_numbers = 0

for numbers in range(1,101):
    if  numbers % 3 ==0  and numbers % 5== 0:
        print("FizzBuzz")
    elif  numbers % 5== 0:
        print("Buzz")
    elif  numbers % 3 ==0  :
        print("Fizz")
    else :
        print(numbers)