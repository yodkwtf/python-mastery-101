def add_positive_nums(x,y):
  assert x > 0 and y > 0, "Both the numbers must be positive"
  return x+y

print(add_positive_nums(2, 5)) # 7
add_positive_nums(3, -5) # AssertionError: Both the numbers must be positive