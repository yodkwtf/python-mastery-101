## Functions

A function is a block of code that performs similar tasks every time it is called. It can take inputs and returns output when the return keyword is used.

```py
# defining a function
def name_of_function():
  # all the code
  print('Hi')

# invoking function by calling it
name_of_function() # Hi
```

#### THE `RETURN` KEYWORD

- returns/export a value from a function that can be stored in a variable to use it later
- it exits the function right away and anything below it will be ignored
- it pops the function off the call stack
- we can return anything and not just a single item

```py
def greet_user():
  return 'Hello Sir!'

# getting returned value
greeting = greet_user()
print(greeting) # Hello Sir!
```

#### PARAMETER

Functions accept input and perform the tasks based on those inputs. It makes them more dynamic and reusable.

```py
def square(num):
  return num**2

print(square(4)) # 16
print(square(6)) # 36
```

- If we create a parameter while defining functions, we must also pass argument when calling it otherwise there will be an error.
- We can have as many parameters as we want by separating them with comma

  ```py
  def add(a,b):
    return a+b

  print(add(4, 8)) # 12
  print(add(6, 6)) # 12
  ```

- It's better to have relevant parameter names

##### Parameters vs Arguments

Parameters are the variable in a method definition, when a function is defined, whereas
Arguments are the data we pass into while calling the function

For example, in the above code block, `a` and `b` are the parameters where as `4` and `8` are the arguments

#### DEFAULT PARAMETERS

- we can set up a default value for parameters so if we don't provide an argument, the function runs w the default parameter and doesn't throw an error
- if we do provide an argument, the function overwrites the default parameter

```py
def exponent(num, power = 2): # default value as 2
  return num**power

print(exponent(2,5)) # 2**5 = 32
print(exponent(4)) # 4**2 = 16
```

- allows you to be more defensive and helps avoid error with incorrect parameters
- default parameters can be anything from a string to list, dictionary, booleans or even another function
- parameters are assigned in order so try to it set it up at the end or make sure each parameter has a default value

#### KEYWORD ARGUMENTS

- can be used to specify which argument corresponds to which parameter
- hence, the order of the arguments doesn't matter anymore

```py
def expo(x, y):
  return x**y

# normal
print(expo(3, 2)) # 9
print(expo(2, 3)) # 8

# keyword arguments
print(expo(y=2, x=3)) # 9
```

When we use **=** while defining a function, we set up a default parameter whereas when we use **=** while invoking a function we make a keyword argument

#### PARAMETER ORDERING

If we're gonna have all of these things in a function, this is the order they should follow

1. parameters
2. \*args
3. default parameters
4. \*\*kwargs

In case we have both `*args` and `default parameters` then we would need to pass the values for default parameters as keyword arguments otherwise `*args` will eat up those arguments.

---

## args and kwargs

#### \*args

- special operator we pass to functions
- gathers any remaining arguments after using it as a tuple
- can be called anything - `*some_name`

```py
# when we no. of parameters to be passed
def sum_all_nums(a, b, c):
  return a+b+c

print(sum_all_nums(2,5,7)) #14

# when no. of parameters isn't fixed
def sum_nums(*args):
  total=0
  for num in args:
    total += num
  return total

print(sum_nums(2,5,3)) #10
print(sum_nums(1,2,3,4,5)) #15
```

- we can have as many arguments as we want without having corresponding parameters for them

#### \*\*kwargs

- special operator passed w functions
- looks for keyword arguments
- gathers all the remaining keyword arguments after it is used into a dictionary
- can be called anything we want - `**some_name`

```py
def fav_colors(**kwargs):
  for k, v in kwargs.items():
    print(f"{k}'s fav color is {v}")

fav_colors(durgesh="red", john="black", tanu="pink")
'''
durgesh's fav color is red
john's fav color is black
tanu's fav color is pink
'''
```

- we can pass as many keyword arguments and it'll print the fav color for each of them

---

## Scope

- where our variables can be accessed
- whenever we define a variable inside a func, it can only be used inside the function

#### Global

- when we have variables outside a function they are called global
- we can alter a global value from inside a function in the usual way
- we need to use `global` keyword to reference the variable from global scope (here we basically tell function that we want to use global variable cuz by default function looks for a local variable)

  ```py
  total = 0

  def inc():
      global total # if we don't have this line, we get an error
      total+=1
      return total

  inc()
  ```

- we don't need to use `global` keyword if we only want to access and not change it

#### nonlocal

- lets us modify a parent's variables in a child (nested) function
  ```py
  def outer():
    count = 0
    def inner():
      nonlocal count # tells function we're not looking for a local variable (works similar to global)
      count += 1
      return count
    return inner()
  ```
- works similar to `global` keyword but used for cases like above where a parent's variable needs to be manipulated but it's not in the global score

---

## Documenting Functions

- **Doc Strings** can be used to explain what a function does
- use `""" msg """` inside a function to write a doc string
- they can even be accessed using `function_name.__doc__`

  ```py
  def say_hello():
    """ A simple function to return a hello msg to user"""
    return "Hello Friend!"

  print(say_hello()) # Hello Friend!
  print(say_hello.__doc__) # A simple function to return a hello msg to user
  ```

- we can see the doc string even for the built-in functions
  `print(print.__doc__)`

---
