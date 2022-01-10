from random import randint

random_number = randint(1,10)

guess = int(input("Guess the number bw 1 and 10:\n> "))

while guess != random_number:
  if guess > random_number:
    print("Too high, try again!")
  else:
    print("Too low, try again!")
  guess = int(input("Guess the number bw 1 and 10:\n> "))
else:
  print("You guessed it! You won!")
