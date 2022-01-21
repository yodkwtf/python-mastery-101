 ## all 
print(all([0,1,3,4])) # False, since 0 is falsy

names = ["John", "Jack", "Jay"]
is_J_first = [name[0]=="J" for name in names]

print(is_J_first) # [True, True, True]
print(all(is_J_first)) # True

## any

print(any([0, '', 4, None])) # True, since 4 is truthy