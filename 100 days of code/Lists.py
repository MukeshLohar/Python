# 🚨 Don't change the code below 👇
row1 = ["X","X","X"]
row2 = ["X","X","X"]
row3 = ["X","X","X"]
asd = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print(asd)
#position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position ="31"
result_column = int(position[0]) - 1
result_row = int(position[1]) - 1

asd[result_row][result_column] = "O"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")