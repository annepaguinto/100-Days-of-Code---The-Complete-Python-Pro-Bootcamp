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

choices = [rock, paper, scissors]
choice_name = ["Rock", "Paper", "Scissors"]
player_choice = int(input("Rock, Paper, Scissors. Select 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0,2)

if player_choice > 2 or player_choice < 0:
    player = ""
else:
    player = choices[player_choice]
    computer = choices[computer_choice]

    print(player)
    print("You chose " + choice_name[player_choice])

    print(computer)
    print("Computer chose " + choice_name[computer_choice])

if player_choice > 2 or player_choice < 0:
    print("Invalid input")
elif choice_name[player_choice] == "Rock" and choice_name[computer_choice] == "Scissors":
    print("You win")
elif choice_name[player_choice] == "Paper" and choice_name[computer_choice] == "Rock":
    print("You win")
elif choice_name[player_choice] == "Scissors" and choice_name[computer_choice] == "Paper":
    print("You win")
elif player_choice == computer_choice:
    print("\nIt's a draw. Try again.")
else:
    print("You lose")
