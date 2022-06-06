class Animal:
  cool = True

  def make_sound(self, sound):
    print(f"This animal says {sound}")

class Cat(Animal):
  pass

a = Animal()
a.make_sound("woof")

pussy = Cat()
pussy.make_sound("meow") # we can call the method from the parent class

print(pussy.cool) # True
print(Cat.cool) # True
print(Animal.cool) # True