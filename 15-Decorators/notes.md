## Higher Order Functions

- We can pass functions as arguments inside other functions
- We can also nest functions inside other functions
- We can also return functions from other functions
- Inner functions can access outer functions scope (variables) aka **closure**

> Colt Steele's "Python Course - Higher Order Functions" video has a great example of closure

## Decorators

- Decorators are functions that wrap other functions enhancing their behaviors
- They then return the wrapper function, not the func that has been wrapped
- They are examples of Higher Order Functions
- They have their own special syntax `using @` (syntactic sugar), though it's not mandatory to use them

## Decorators with Different Signatures

What to do if the wrapped functions take different number of arguments?

In such cases we pass **args** and **kwargs** as the function parameters for the wrapper function so it can take none to any number of arguments.

```py
# BOILER PLATE FOR A DECORATOR FUNCTION

from functools import wraps

def main(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    # some tasks
    result = fn(*args, **kwargs)
    # some tasks
    return result
  return wrapper

@main
def function_name():
  return 'something'

function_name()
```

## Decorators Functions Taking Arguments

- We can also create decorator functions that take arguments
- We have to add an extra layer of function which will take the argument passed and return a new wrapper function to wrap our fn to be wrapped

```py
from functools import wraps

def main(val):

  def inner(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      # do something with `val` maybe
      result = fn(*args, **kwargs)
      # some tasks
      return result
    return wrapper
  return inner

@main(some_val)
def function_name():
  return 'something'

function_name()
```
