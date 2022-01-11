numbers = [1,2,3,4,5,6]

# store even values
evens = [num for num in numbers if num % 2 == 0] # [2,4,6]

# if even, double it and if odd, half it
weird = [num*2 if num%2==0 else num/2 for num in numbers] # [.5, 4, 1.5, 8, 2.5, 12]

print(evens)
print(weird)