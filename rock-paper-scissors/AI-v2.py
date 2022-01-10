from random import randint

p_score, c_score, win_score = 0, 0, 3

while p_score < win_score and c_score < win_score:
  
  print(f"\n*************************\nPlayer score: {p_score} Computer Score: {c_score}")

  print("...Rock...")
  print("...Paper...")
  print("...Scissors...")

  player = input("Player (Enter your move): ").lower()

  if player == "quit" or player == "q":
    break

  rand_num = randint(0, 2)
  if rand_num == 0:
    computer = "rock"
  elif rand_num == 1:
    computer = "paper"
  else:
    computer = "scissors"

  print(f'Computer plays {computer}')

  if player == computer:
    print("It's a tie mf!")

  elif player == "rock":
    if computer == "scissors":
      print("You win!")
      p_score +=1
    else:
      print("Computer won :/")
      c_score +=1

  elif player == "paper":
    if computer == "rock":
      print("You win!")
      p_score +=1
    else:
      print("Computer won :/")
      c_score +=1

  elif player == "scissors":
    if computer == "paper":
      print("You win!")
      p_score +=1
    else:
      print("Computer won :/")
      c_score +=1

  else:
    print("Please enter a valid move dumbass...")

if p_score > c_score:
  print("Congrats, You won!")
else:
  print("OH NO, Computer won!")
