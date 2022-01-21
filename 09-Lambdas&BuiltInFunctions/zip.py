nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

z = zip(nums1, nums2)

print(z) # <zip object at 0x0000022F88BE3600>
print(list(z)) # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(dict(zip(nums1, nums2))) # {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

## Unpacking inside zip 
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]

z = list(zip(*five_by_two)) 
print(z) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]