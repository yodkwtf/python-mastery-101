# defining class
class User:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def initials(self, thing):
    return f"{self.first_name[0]}.{self.last_name[0]}. likes {thing}"

# instances
john = User("john", "doe")
mary = User("mary", "lopez")

# calling instance methods
print(john.full_name())
print(mary.initials('banana'))