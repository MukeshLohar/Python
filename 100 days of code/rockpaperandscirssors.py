import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_input = int(input("What do you want to choose? Type 0 for Rock,1 for Paper or 2 for Scissors \n"))

sample_set= [ rock, paper,scissors]

computer_generated = sample_set[random.randint(0,2)]

if user_input == 0 :
    user_generated = sample_set[user_input]
    print(f'You Choose : {user_generated} )
elif user_input == 1 :
    user_generated = sample_set[user_input]
    print(f'You Choose : {user_generated}') 
elif user_input == 2 :
    user_generated = sample_set[user_input]
    print(f'You Choose : {user_generated}') 
else:
    print("Wrong choice ! you lost")

print(f"Computer choose : \n {computer_generated}")




# rock > scissors> paper> rock
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.


if (user_generated == rock and computer_generated == scissors) or (user_generated == scissors and computer_generated == paper) or (user_generated == paper and computer_generated == rock) :
    print(f'Yahoo!! you Win')
elif (computer_generated == rock and user_generated == scissors) or (computer_generated == scissors and user_generated == paper) or (computer_generated == paper and user_generated == rock) :
    print(f'Sad !!You lose')
else:
    print(f'No one Wins, Draw!!')