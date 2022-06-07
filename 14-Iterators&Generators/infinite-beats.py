# Lame function that returns a list of beats.  
# Only runs 100 times
def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0
		result.append(nums[i])
		i += 1
	return result

# Infinite Generator - returns one beat a time, no list used!
# we can call the next method whenever we need the next beat and the function won't re-run. we'll just get the next beat
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

