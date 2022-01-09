from random import randint

player = input("Player (Enter your move): ").lower()

rand_num = randint(0, 2)

if rand_num == 0:
  computer = "rock"
elif rand_num == 1:
  computer = "paper"
else:
  computer = "scissors"

print(f'Computer plays {computer}')


# more nested setup than v1
if player == computer:
  print("It's a tie mf!")

elif player == "rock":
  if computer == "scissors":
    print("You win!")
  else:
    print("Computer won :/")

elif player == "paper":
  if computer == "rock":
   print("You win!")
  else:
    print("Computer won :/")

elif player == "scissors":
  if computer == "paper":
    print("You win!")
  else:
    print("Computer won :/")

else:
  print("Please enter a valid move dumbass...")
