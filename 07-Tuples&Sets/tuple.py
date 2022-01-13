alphabet = ('a', 'b', 'c')

print(type(alphabet))

# iterating over tuples
for letter in alphabet:
  print(letter)

# using tuples as keys in dictionaries
locations = {
  (35.6895, 39.6917): "Tokyo Office",
  (40.7128, 74.0060): "New York Office"
}

print(locations[(40.7128, 74.0060)])