class Chicken:
  total_eggs = 0

  def __init__(self, name, species, eggs = 0):
    self.name = name
    self.species = species
    self.eggs = eggs

  def lay_egg(self):
    Chicken.total_eggs += 1
    self.eggs += 1
    return self.eggs