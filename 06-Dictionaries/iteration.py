cat = {
  "name": "Kitty",
  "age" : 5,
  "isCute": True
}

# iterating over values to get values
for value in cat.values():
  print(value)

# iterating over keys to get keys
for key in cat.keys():
  print(key)

# iterating over items to get key-value pairs
for key,value in cat.items():
  print(f"{key}: {value}")