d = {"name": "Ricky"}

def get(d, key):
  try:
    return d[key]
  except KeyError: # Catching specific errors
    return None

print(get(d, "name"))
print(get(d, "city"))

#! This mimics the `get` method on dictionaries except this is a separate function and not a method on `d`