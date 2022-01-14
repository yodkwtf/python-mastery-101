from random import random

def flip_coin():
  # get a random no. from 0-1
  r = random()
  # create `head` or `tails` based on `r`
  if r > 0.5:
    return 'HEADS'
  else:
    return 'TAILS'

print(flip_coin())