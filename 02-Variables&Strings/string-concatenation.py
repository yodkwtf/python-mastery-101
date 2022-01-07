str_one = "Ice"
str_two = "Cream"

# concatenation
print("I like " + str_one + " " + str_two)

# formatter strings
guess = 8

print(f"Your guess of {guess} is incorrect") # we can't do this with above way

# we can also do some math here
print(f"{guess * 2} is incorrect")

# convert number to string
new = str(guess)
print(type(new))
