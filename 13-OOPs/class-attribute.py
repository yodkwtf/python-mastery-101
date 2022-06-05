# defining class
class User:
  # define a class attribute
  active_users = 0

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    # add 1 to the class attribute
    User.active_users += 1

  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def initials(self, thing):
    return f"{self.first_name[0]}.{self.last_name[0]}. likes {thing}"


# initial value of class attribute
print(User.active_users)

# create instances
john = User("john", "doe")
mary = User("mary", "lopez")

# final value of class attribute
print(User.active_users)