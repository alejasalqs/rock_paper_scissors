import os
import random

player_lifes = 3
computer_life = 3

rock_sprite = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer choose rock!
"""

paper_sprite = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

Computer choose paper!
""" 

scissors_sprite = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Computer choose scissors!
"""

def check_if_winner():
  if player_lifes == 0:
    print("Computer Win")
    return True
  elif computer_life == 0:
    print("You Win")
    return True
  else:
    return False

def get_winner(user_option, computer_option):
  global player_lifes
  global computer_life

  
  if user_option == computer_option:
    print("Tie!")
  elif user_option == 'R' and computer_option == 'P':
    print("Computer wins!")
    player_lifes -= 1
  elif user_option == 'P' and computer_option == 'S':
    print("Computer wins!")
    player_lifes -= 1
  elif user_option == 'S' and computer_option == 'R':
    print("Computer wins!")
    player_lifes -= 1
  elif user_option == 'P' and computer_option == 'R':
    print("You win!")
    computer_life -= 1
  elif user_option == 'S' and computer_option == 'P':
    print("You win!")
    computer_life -= 1
  elif user_option == 'R' and computer_option == 'S':
    print("You wins!")
    computer_life -= 1

def verify_users_option(option):
  user_option = ""

  if option == 'R':
    print("Rock")
  elif option == 'P':
    print("Paper")
  elif option == 'S':
    print("Scissors")

  computer_option = define_computer_option()
  get_winner(option,computer_option)


def define_computer_option():
  computer_option = random.randrange(3)

  print(computer_option)

  if computer_option == 0:
    print(rock_sprite)
    return 'R'
  elif computer_option == 1:
    print(paper_sprite)
    return 'P'
  elif computer_option == 2:
    print(scissors_sprite)
    return ('S')


def load_screen():
  print("Type a letter to select your option:")
  print("(R) Rock)")
  print("(P) Paper)")
  print("(S) Scissors)")
  verify_users_option(raw_input("Type option: ").upper())  


while check_if_winner() == False:
  print("Computer lifes" + str(computer_life))
  print("Youer lifes" + str(player_lifes))
  print("Type a letter to select your option:")
  print("(R) Rock)")
  print("(P) Paper)")
  print("(S) Scissors)")
  verify_users_option(raw_input("Type option: ").upper())