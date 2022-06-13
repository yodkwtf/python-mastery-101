def be_polite(fn):
  def wrapper():
    print("What a pleasure to meet you!")
    fn()
    print("Have a great day!")
  return wrapper

# functions to be passes inside the higher order function
def greet():
  print("My name is Deekayy")

def rage():
  print("I HATE YOU IDIOT!")

polite_greet = be_polite(greet)
polite_rage = be_polite(rage)

polite_greet()
polite_rage()