# EXAMPLE 1 - Filter out the evens from the list
nums = [1, 2, 3, 4, 5]

even_nums = filter(lambda n: n % 2 == 0, nums)

print(even_nums)
print(list(even_nums))