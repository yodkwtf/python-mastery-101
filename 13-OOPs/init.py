class User:
  def __init__(self, name):
    self.name = name

# create instances
user1 = User('john') # self.name = 'john' -> user1.name = 'john'
user2 = User('betty')

print(user1.name)
print(user2)