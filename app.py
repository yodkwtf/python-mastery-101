import keyword
 
def contains_keyword(*args):
    for item in args:
      print(item)
      if keyword.iskeyword(item): return True
    return False

r1 = contains_keyword('return', 'hello')
r2 = contains_keyword('orca', 'shark', 'return')

print (r1)
print (r2)