# function for creating custom loop
def my_for(iterable, func):
  # convert arg into iterator
  iterator = iter(iterable)

  # run func for every single item
  while True:
    try:
      # get items one by one
      item = next(iterator)
      # run the func on them
      func(item)

    # stop when items run out
    except StopIteration:
      print('End of loop')
      break

# a normal function
def square(n):
  print(n*n)

my_for("Hello", print)
my_for([1, 2, 3, 4], square)