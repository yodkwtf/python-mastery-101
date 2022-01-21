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