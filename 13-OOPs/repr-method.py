# defining class
class User:
  active_users = 0

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    # add 1 to the class attribute
    User.active_users += 1

  # repr method -> returns a string representation of the object
  def __repr__(self):
    return f"{self.first_name} {self.last_name}"

  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def initials(self, thing):
    return f"{self.first_name[0]}.{self.last_name[0]}. likes {thing}"


# create instances
john = User("john", "doe")
mary = User("mary", "lopez")

# w/o repr method
# print(john) # <__main__.User object at 0x000001FE7C3BFEE0>

# with repr method
print(john) # john doe