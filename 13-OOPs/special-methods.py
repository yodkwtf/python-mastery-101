class Human:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age

  def __repr__(self):
    return f"Human name: {self.first} {self.last}, age: {self.age}"

  # rewriting a special method
  def __add__(self, other):
    if isinstance(other, Human):
      return Human(first = "Newborn", last = self.last, age=0)
    return "You can't add that!"

# create 2 humans
jane = Human("Jane", "Goodall", 39)
john = Human("John", "Doe", 45)

print(jane + john) # add in-turn calls __add__ method which is overwritten in Human class