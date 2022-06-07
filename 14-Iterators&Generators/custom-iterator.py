class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
    # if cur value is less than max one
		if self.current < self.high:
      # get that value
			num = self.current
      # inc it for next iteration
			self.current += 1
      # return it for current iteration
			return num
		raise StopIteration



# for loop calls the iter method on counter which returns self
# then on each iteration our custom `next` method is called
for x in Counter(50,70):
	print(x)