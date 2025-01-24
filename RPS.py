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
game_images = [rock,paper,scissors]
user_choice = int(input("ENTER 0 FOR ROCK , 1 FOR PAPER AND 2 FOR SCISSORS!"))
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer Chose:")
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
    print("ENter correct input")
elif user_choice == 0 and computer_choice==2:
    print("you won!!")
elif user_choice==2 and computer_choice==0:
    print("computer won!!")
elif user_choice > computer_choice:
    print("You Won!!")
elif user_choice<computer_choice:
    print("Computer Won!!")
elif user_choice==computer_choice:
    print("IT's A TIE!!")
else :
    print("please enter correct input")
