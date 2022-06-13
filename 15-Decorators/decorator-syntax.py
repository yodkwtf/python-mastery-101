def be_polite(fn):
  def wrapper():
    print("What a pleasure to meet you!")
    fn()
    print("Have a great day!")
  return wrapper

@be_polite # this is a decorator, now the greet function is already wrapped around the `be_polite` func and we can directly call the `greet` func
def greet():
  print("My name is Deekayy")

def rage():
  print("I HATE YOU IDIOT!")

greet()

# if we wanted to doi it for the rage function too, we'd have to add it above rage function too