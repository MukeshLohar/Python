# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
score1 = int()
score2 = int()

combined_name = (name1 + name2).lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

lovescore = int(f"{true}{love}")
print(lovescore)

if lovescore < 10 and lovescore > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif lovescore > 40 and lovescore < 50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")