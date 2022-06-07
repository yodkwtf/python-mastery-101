def get_unlimited_multiples(number=1):
  i = 1
  while True:
    yield number*i
    i+=1