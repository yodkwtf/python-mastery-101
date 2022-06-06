# PARENT CLASS
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def __repr__(self):
    return f"{self.name} is a {self.species}"

  def make_sound(self, sound):
    print(f"This animal says {sound}")

# CHILD CLASS
class Cat(Animal):
  def __init__(self, name, breed, toy):
    super().__init__(name, species = "Cat") # super() is used to call the parent class
    self.breed = breed
    self.toy = toy