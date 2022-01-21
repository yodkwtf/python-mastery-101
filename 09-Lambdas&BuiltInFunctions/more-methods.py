 ## SORTED 
numbers = (6, 3, 12, 15, 11)

print(sorted(numbers)) # [6, 11, 12, 15]
print(sorted(numbers, reverse=True)) # [15, 12, 11, 6, 3]

## MAX & MIN 
print(max([2,98,3,4, 97.9]))

names = ["Deekayy", "John", "Peter", "Tim"]

min1 = min(len(name) for name in names) # collects the length of all names and returns the smallest one

min2 = min(names, key = lambda n: len(n)) # checks the length of all names and returns the one that has min length

print(min1)
print(min2)

## REVERSED 
for letter in reversed("hello"):
  print(letter) # 'o' 'l' 'l' 'e' 'o'

rev = "".join(list(reversed("hello")))
print(rev) # 'olleh'

## ABS 
print(abs(-25)) # 25
print(abs(-75/8)) # 9.375
print(abs(2.35)) # 2.35

## SUM 
print(sum([1,2,3])) #6
print(sum([1,2,3], 10)) # 10 + (1+2+3) = 16
print(sum([1,2,3], -8)) # ( -8 + (1+2+3)) = -2

## ROUND 
print(round(10.2)) # 10
print(round(-5.6)) # (-6)
print(round(75/7)) # 11
print(round(75/7, 3)) # 10.714
