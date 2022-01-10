from random import randint

random_number = randint(1,10)

while True:
  guess = int(input("Guess a number bw 1 and 10:\n> "))
  if guess > random_number:
    print("Too high, try again!")
  elif guess < random_number:
    print("Too low, try again!")
  else:
    print("You guessed it! You won!")
    play_again = input("Wanna play again? (y/n) ")

    if play_again == "y":
      random_number = randint(1,10)
      guess = int(input("Guess a number bw 1 and 10:\n> "))
    else:
      print("Thank you for playing!")
      break
