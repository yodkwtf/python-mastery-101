# Ask user how many km he ran and convert it into miles

print("how many kms did you run today?")
kms = input("> ") # it returns a string

miles = float(kms) / 1.60934
miles = round(miles, 2)

print(f"Okay your {kms} kms are {miles} miles")