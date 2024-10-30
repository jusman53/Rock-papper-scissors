#rock paper scissors game
import random
scissors = ('''
     .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
''')
paper = ('''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'  
''')
rock = ('''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
''')
game = [rock, paper, scissors]
player_choice = int(input("Please enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.choice(game)
if not 0 <= player_choice <= 2: 
    print("You have not entered a valid Choice")
    exit()
print("You chose" + game[player_choice])
print("Computer chose" + computer_choice)
if player_choice == 0 and computer_choice == game[0]:
    print("It's a Draw!!!")
elif player_choice == 0 and computer_choice == game[1]:
    print("Computer Wins!!!")
elif player_choice == 0 and computer_choice == game[2]:
    print("You Win!!!")
elif player_choice == 1 and computer_choice == game[0]:
    print("You Win!!!")
elif player_choice == 1 and computer_choice == game[1]:
    print("It's a Draw!!!")
elif player_choice == 1 and computer_choice == game[2]:
    print("Computer Wins!!!")
elif player_choice == 2 and computer_choice == game[0]:
    print("Computer Wins!!!")
elif player_choice == 2 and computer_choice == game[1]:
    print("You Win!!!")
elif player_choice == 2 and computer_choice == game[2]:
    print("It's a Draw!!!")
