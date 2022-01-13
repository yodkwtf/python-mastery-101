# EXAMPLE 1
numbers = dict(first = 1, second = 2, third = 3)

squared = {key:value**2 for key,value in numbers.items()}
print(squared)

# EXAMPLE 2
str1 = "ABC"
str2 = "123"

combo = {str1[i]: str2[i] for i in range(0, 3)}
print(combo)

# EXAMPLE 3 - YELL
instructor = dict(name="Durgesh", city="Gurgaon", color="red")

yell_instructor = {k.upper(): v.upper() for k,v in instructor.items()}
print(yell_instructor)