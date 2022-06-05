# defining class
class User:
  active_users = 0

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    User.active_users += 1

  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def initials(self, thing):
    return f"{self.first_name[0]}.{self.last_name[0]}. likes {thing}"

  # class method
  @classmethod
  def display_active_users(cls):
    return f"There are currently {cls.active_users} active users"


# initial active users
print(User.display_active_users())

# create instances
john = User("john", "doe")

# middle active users
print(User.display_active_users())

mary = User("mary", "lopez")

# final active users
print(User.display_active_users())
