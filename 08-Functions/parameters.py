 ## PARAMETERS
def cube(num):
  return num**3

print(cube(2))
print(cube(11))

## DEFAULT PARAMETERS
def exponent(num, power = 2): # default value as 2
  return num**power

print(exponent(2,5)) # 2**5 = 32
print(exponent(4)) # 4**2 = 16

## KEYWORD ARGUMENTS
def expo(x, y):
  return x**y

print(expo(3, 2)) # 9
print(expo(2, 3)) # 8
print(expo(y=2, x=3)) # 9