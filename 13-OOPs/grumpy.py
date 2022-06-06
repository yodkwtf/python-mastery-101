class GrumpyDict(dict):
  def __repr__(self):
    print("NONE OF YOUR BUSINESS")
    return super().__repr__() # prints the normal way of dict

  # over writing magic method which is called when you try to access a key that doesn't exist
  def __missing__(self, key):
    print(f"YOU WANT {key}? WELL IT AIN'T HERE!")

  # over writing magic method called when dict value is updated
  def __setitem__(self, key, value):
    print("YOU WANT TO CHANGE THE DICTIONARY? OKAY!")
    super().__setitem__(key, value) # calling magic method on dict class

# create an instance of GrumpyDict
data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)

data['city'] = "New York"

print(data)