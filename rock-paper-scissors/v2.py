print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

# more nested setup than v1
if player2 == "rock" or  player2 == "paper" or  player2 == "scissors": 
  if player1 == player2:
    print("It's a tie mf!")

  elif player1 == "rock":
    if player2 == "scissors":
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")

  elif player1 == "paper":
    if player2 == "rock":
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")

  elif player1 == "scissors":
    if player2 == "paper":
      print("Player 1 wins!")
    else:
      print("Player 2 wins!")

  else:
    print("Player 1, please enter something valid...")

else:
  print("Player 2, please enter something valid...")