 ## TUPLE UNPACKING
def sum_all_nums(*args):
  total = 0
  for num in args:
    total += num
  print(total)

nums = [1,3,2,4]

sum_all_nums(1,3,4,5)
sum_all_nums(*nums)

## DICTIONARY UNPACKING
def display_names(first, second):
  print(first, second) 

name = {"first": "John", "second":"Doe"}

display_names(first="Colt", second="Steele")
# display_names(name) 
display_names(**name)


def add_nums(a,b,c,**kwargs):
  print(a+b+c)
  print('some more code')
  print(kwargs)

dict1 = dict(a=1, b=2, c=5) 
dict2 = dict(a=1, b=2, c=5, d=15, name="Ron") 

add_nums(**dict1)
'''
8
some more code
{}
'''

add_nums(**dict2)
'''
8
some more code
{'d': 15, 'name': 'Ron'}
'''