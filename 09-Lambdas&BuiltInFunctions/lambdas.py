# normal function
def square (num): return num**2

# lambda function
square2 = lambda num: num**2

print(square(2)) # 4
print(square2(3)) # 9

# checking their names
print(square.__name__) # square
print(square2.__name__) # lambda