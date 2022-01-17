 ## when we no. of parameters to be passed
def sum_all_nums(a, b, c):
  return a+b+c

print(sum_all_nums(2,5,7)) #14

 ## when no. of parameters isn't fixed
def sum_nums(x, y, *remaining_nums):
  # we can still have other parameters for different tasks
  print(x,y)

  total=0
  for num in remaining_nums:
    total += num
  return total

print(sum_nums(13, 11, 2,5,3)) #10
print(sum_nums(6,7,1,2,3,4,5)) #15

