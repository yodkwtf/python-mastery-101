nums = [2,4,5,6,8]

doubles = map(lambda n: 2*n, nums)

print(doubles) # <map object at 0x000001B8AF75EDA0>
print(list(doubles)) # [4, 8, 10, 12, 16]


# ANOTHER EXAMPLE
people = ["Darcy", "Christine", "John"]

peeps = list(map(lambda name: name.upper(), people))
print(peeps)