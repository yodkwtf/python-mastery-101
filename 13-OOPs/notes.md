## Object Oriented Programming (OOPs)

- Encapsulation & Abstraction
- Classes and instances
- Attaching methods and properties to classes

#### What is OOP?

- Most programming have OOP, not python specific
- Method of programming that attempts to model some process/thing in the world as a **class** or **object**
- Kinda allows us to create our own type

#### Classes

- A blueprint for objects
- Can contain methods and attributes (similar to keys in a dict.)
- For eg, a user class is a blueprint for every individual user we create

#### Object

- Instance of a class (based on the class blueprint)
- Has the methods and properties of the class
- There are so many built-in classes too
- For eg, every list we create is an instance of the class _list_ and every list method comes from the list class

## Why OOP?

- An easier way to organize and structure our code in a more humanly way
- Everything can be grouped into different classes
- Isn't a compulsion, there are languages that don't even support OOP and can still do all the same things
- Breaking things down and classifying them

#### Encapsulation

- Grouping of public and private attributes into a class

##### _private attributes_

- are the properties that don't need to be exposed (used) outside a class
- we can use them but it's a convention to let other devs know that we shouldn't
- their names starts with an underscore (\_cards)

#### Abstraction

- Exposing only "relevant" (bare min.) data from a class, hiding private attributes and methods (aka inner workings)

## Classes & Objects

- we can create empty classes using `pass` keyword
- if 2 instances of a class are same, they still point to different place in memory

#### Naming Convention for Classes

- Created with the keyword `class`
- Use CamelCase - convention not compulsion
- Should be singular - User not Users

#### Instance Attributes

- Classes have a special **\_\_init\_\_** method which gets called every time we create an instance of that class
- `init` method takes a parameter called **self** which points to that particular instance of a class we're working with
- Doesn't have to be called self but it's common convention
- This init method creates all the instance attributes

#### Instance Methods

- we can add functions to classes which are called methods
- these functions can be accessed by all the instances of that class
- we must pass **self** as the first parameter to all the methods even when there's no use of it, python is expecting it or else it'll throw an error
- we can also mutate the pre defined attributes inside these methods

#### Class Attributes

- Lives on the class itself rather than defined by the instance
- Shared by all the instances
- Only defined once
- Used far less than instance attr.
- Can be defined right above all instance att. w/o needing the **self** keyword
- Can be used as an attribute on the individual instances too

#### Class Methods

- Not concerned w instances, but the class itself
- Not used that often, very rare
- Prefixed with the **@classmethod** decorator
- Used when we don't need any data about the instances & we're doing something on the class level
- The class itself is passed as an argument (just like _self_ but conventionally called **cls**)
- Common use case can be validating, or converting coming data from one form to another before creating a new instance from that data

#### Repr Method

- Another dunder method `__repr__(self)`
- Allows us to format what we return from an instance into a readable string
- Whatever we return from this func is the default return when we print that instance otherwise we get the instance in an unreadable format
- Can change `<__main__.User object at 0x000001FE7C3BFEE0>` to `john doe`

##### _Underscores, Dunder Methods, etc._

- `__init__` called dunder methods
- have double underscore on both sides
- special methods python looks for

---

- `__msg` - called name mangling
- python changes the names of these variables behind the scenes
- basically `__msg` inside a `User` class gets renamed to `_User__msg` instead
- makes a attribute particular to a class to avoid name collision during inheritance

---

- `_name` - a convention to write private attributes
- there's no such thing as an actual pvt attr. in python but it's for other devs to alert them
- there pvt attr. can only be used by other attr. internally inside classes/functions

## Inheritance

- When a class inherits properties from another class (base or parent class)
- Done by passing the parent class as na argument when defining child class
- Multiple inheritance is also possible
  - child element can inherit properties from multiple parent classes
  - the order in which parent classes are passed matters
  - not that commonly used

## Properties

- Makes it easy to work with methods inside classes as we don't have to call them with arguments
- They can just be accessed like attributes
- Decorators are used above the methods for this purpose
- Kinda like syntactic sugar

## Super()

- Used to call the parent class inside the child's init method
- Automatically passes _self_ as the first argument
- Helps reduce code duplication as we don't have to call separate init for all the child classes

```
super().__init__(name, species) ✅
Animal.__init__(self, name, species) ❌
```

## Method Resolution Order (MRO)

- When a class is created python sets up MRO behind the scenes
- It is the order in which python will look for methods on instances of the class
- A lot of complexity behind the scenes on python decides the order
- MRO can be referenced in 3 ways -
  - **\_\_mro\_\_** dunder attribute on class
  - **mro()** method on class
  - builtin **help(cls)** method -> most readable way
- Not that common topic

## Polymorphism

- An object can take on many(poly) forms(morph)
- Two most important practical applications
  - same class method works similar way for different classes
    eg. a speak method on class Dog, Cat, etc.
  - same operation working for different kinds of objects
    eg. len('string'), len([1,2,3])

## Special Methods

- Called magic methods, tell python how to handle certain operations behind the scenes
- All of them are dunder methods
- Can be overwritten inside classes
- Can allow us to mutate how certain operations work in python
